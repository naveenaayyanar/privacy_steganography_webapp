 Behind Closed Doors

Behind Closed Doors is a privacy-focused web application that allows you to securely hide and extract secret text messages inside various file types using steganography techniques. Built with an emphasis on elegant, modern design and developer-friendly experience, the app adheres strictly to minimal and sophisticated UI principles to provide clarity, trust, and ease of use.



 Features

- Hide secret text inside files including `.doc`, `.xel`, `.exe`, `.png`, `.pdf`, `.jpeg`, and more.
- Extract hidden text messages from steganography-enabled files easily.
- Supports client-friendly file uploads and downloads.
- Modern, elegant UI designed according to Default Design Guidelines:
  - Light background (ffffff) with ample whitespace.
  - Bold typography for strong visual hierarchy.
  - Neutral gray body text (6b7280) for readability.
  - Subtle rounded corners and light shadows for card layouts.
  - Minimal, sticky top navigation with soft transitions.
  - Large hero section with a prominent call-to-action button.
- Uses TailwindCSS utility-first styling for responsive, clean layouts.
- Semantic HTML5 and accessibility minded design.



 Technology Stack

- Backend: Python Flask (web framework for routing and API management)
- Image Processing: Pillow (to embed and extract messages in image files)
- Frontend: Single-page HTML with TailwindCSS for styling and JavaScript for interactivity
- Security: Uses Werkzeug for secure filename handling of uploads



 Installation

To run this project locally, follow these steps:

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/behind-closed-doors.git
   cd behind-closed-doors
   ```

2. Create a Python virtual environment (recommended)  
   - On macOS/Linux:  
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:  
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app  
   ```bash
   python app.py
   ```

5. Open your browser  
   Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to use the application.



 Usage

- Use the Hide Text in File section to upload any supported file and type the secret message you want to embed. Click Hide Text & Download to get your steganography file.
- Use the Extract Text from File section to upload a steganography file and extract the embedded message.
- The UI provides clear feedback on all actions with smooth transitions.



 File Support

- Supported extensions for hiding and extraction:
  - Images: `.png`, `.jpg`, `.jpeg`
  - Documents and binaries: `.doc`, `.docx`, `.xel`, `.exe`, `.pdf`
- For image files, text is embedded using image alpha channel steganography.
- For other files, the message is appended with a secure marker.



 Design Inspiration

Inspired by the Default Design Guidelines for minimal, elegant component library interfaces:

- Full-width responsive layout with centered max-width container (~1200px)
- Generous whitespace and vertical padding for clear visual separation
- Cards with subtle rounded corners (0.75rem) and soft shadows
- Bold headings with strong hierarchy
- Gentle hover and active animations on buttons and cards
- Semantic HTML5 with accessibility considerations



 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open issues or submit pull requests for improvements.



 License

This project is licensed under the MIT License.



 Acknowledgements

Special thanks to the open-source community, Flask, Pillow, and Tailwind CSS for enabling this project.


*Designed and Developed by Naveena*
