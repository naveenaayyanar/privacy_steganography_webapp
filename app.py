import io
import os
from flask import Flask, render_template, request, send_file, jsonify
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'doc', 'docx', 'xel', 'exe', 'png', 'pdf', 'jpeg', 'jpg'}
TEXT_MARKER = b"STEGA_NAVEENA_TEXT_START"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def hide_text_in_image(image_bytes, message):
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert("RGBA")

    message_bytes = message.encode('utf-8')
    message_len = len(message_bytes)
    if message_len == 0:
        return image_bytes

    max_capacity = image.width * image.height
    if (message_len + 4) * 8 > max_capacity:
        raise ValueError("Message too long to hide in this image.")

    pixels = list(image.getdata())
    new_pixels = []
    bit_idx = 0

    message_len_bytes = message_len.to_bytes(4, byteorder='big')
    all_bytes = message_len_bytes + message_bytes

    bits = ''.join(f'{byte:08b}' for byte in all_bytes)
    total_bits = len(bits)

    for i, pixel in enumerate(pixels):
        if bit_idx < total_bits:
            r, g, b, a = pixel
            bit = int(bits[bit_idx])
            a = (a & 0xFE) | bit
            bit_idx += 1
            new_pixels.append((r, g, b, a))
        else:
            new_pixels.append(pixel)

    image.putdata(new_pixels)
    output = io.BytesIO()
    image.save(output, format="PNG")
    return output.getvalue()

def extract_text_from_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert("RGBA")

    pixels = list(image.getdata())

    message_len_bits = ""
    for i in range(32):
        _, _, _, a = pixels[i]
        message_len_bits += str(a & 1)
    message_len = int(message_len_bits, 2)
    if message_len == 0:
        return ""

    total_bits = message_len * 8
    bits = []
    for i in range(32, 32 + total_bits):
        _, _, _, a = pixels[i]
        bits.append(str(a & 1))
    byte_chunks = [bits[i:i+8] for i in range(0, len(bits), 8)]
    message_bytes = bytes(int(''.join(b), 2) for b in byte_chunks)
    try:
        message = message_bytes.decode('utf-8')
    except UnicodeDecodeError:
        message = ""
    return message

def hide_text_in_binary_file(file_bytes, message):
    message_bytes = message.encode('utf-8')
    return file_bytes + TEXT_MARKER + message_bytes

def extract_text_from_binary_file(file_bytes):
    idx = file_bytes.find(TEXT_MARKER)
    if idx == -1:
        return ""
    message_bytes = file_bytes[idx + len(TEXT_MARKER):]
    try:
        message = message_bytes.decode('utf-8')
    except UnicodeDecodeError:
        message = ""
    return message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hide', methods=['POST'])
def hide():
    if 'file' not in request.files or 'message' not in request.form:
        return "Missing file or message", 400

    uploaded_file = request.files['file']
    message = request.form['message'].strip()
    if uploaded_file.filename == '' or not message:
        return "File or message is empty", 400

    if not allowed_file(uploaded_file.filename):
        return "File type not allowed", 400

    filename = secure_filename(uploaded_file.filename)
    file_ext = filename.rsplit('.', 1)[1].lower()
    file_bytes = uploaded_file.read()

    try:
        if file_ext in ('png', 'jpeg', 'jpg'):
            output_bytes = hide_text_in_image(file_bytes, message)
            output_filename = f"steg_{os.path.splitext(filename)[0]}.png"
            return send_file(io.BytesIO(output_bytes), download_name=output_filename, as_attachment=True, mimetype='image/png')
        else:
            output_bytes = hide_text_in_binary_file(file_bytes, message)
            output_filename = f"steg_{filename}"
            return send_file(io.BytesIO(output_bytes), download_name=output_filename, as_attachment=True)
    except Exception as e:
        return f"Error processing file: {str(e)}", 500

@app.route('/extract', methods=['POST'])
def extract():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    filename = secure_filename(uploaded_file.filename)
    file_ext = filename.rsplit('.', 1)[1].lower()
    file_bytes = uploaded_file.read()

    try:
        if file_ext in ('png', 'jpeg', 'jpg'):
            message = extract_text_from_image(file_bytes)
            return jsonify({'message': message or ''})
        else:
            message = extract_text_from_binary_file(file_bytes)
            return jsonify({'message': message or ''})
    except Exception as e:
        return jsonify({'error': f'Error extracting text: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
