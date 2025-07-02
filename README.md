I'll update the README.md file with Termux API information and the current timestamp:

```markdown
# TermPassX - The Ultimate Termux Password Generator

```text
Tool Name: TermPassX - The Ultimate Termux Password Generator
Author: Mahedi Hasan Rafsun
Developer | Programmer | Cybersecurity Enthusiast
Current Version: 1.0.0 (Last Updated: 2025-07-02 01:09:41 UTC)
```

## 📝 Description

TermPassX is a powerful and secure password generator designed specifically for Termux users. It generates cryptographically strong passwords using Python's `secrets` module and provides extensive customization options.

## ✨ Features

- 🔐 Secure password generation using cryptographic methods
- 📏 Customizable password length (8-128 characters)
- 🎯 Multiple character set options:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Numbers (0-9)
  - Special symbols (!@#$%^&*()_+-=[]{}|;:,.<>?)
  - Emojis (😀😎🔒💪🚀⭐️🔑💻🎯)
- 📊 Password strength detection:
  - Weak (< 50 bits entropy)
  - Medium (50-70 bits entropy)
  - Strong (70-90 bits entropy)
  - Very Strong (> 90 bits entropy)
- 📋 Clipboard integration using Termux:API
- 📜 Password history tracking
- 🔍 Password validation tool
- 🎨 Colorful CLI interface
- 🚫 Prevents repeated characters
- ⚡ Generate multiple passwords at once

## 🛠️ Installation

1. First, install Termux:API:
```bash
# Install Termux:API package
pkg install termux-api

# Install Termux:API app
# You must install the Termux:API app from F-Droid
# F-Droid link: https://f-droid.org/packages/com.termux.api/
```

2. Clone the repository:
```bash
git clone https://github.com/mhrtuch240/TermPassX.git
cd TermPassX
```

3. Make the installer executable:
```bash
chmod +x install.sh
```

4. Run the installer:
```bash
./install.sh
```

## 📋 Requirements

### Termux Packages Required:
```bash
pkg install python
pkg install termux-api
pkg install git
```

### Termux:API Features Used:
- `termux-clipboard-set`: For copying passwords to clipboard
- Requires both:
  1. Termux:API package (pkg install termux-api)
  2. Termux:API app (from F-Droid)

### Python Packages:
```bash
pip install colorama
```

## 🚀 Usage

Start the tool by running:
```bash
termpassx
```

### Main Menu Options:
1. Generate Password(s)
   - Choose number of passwords (1-10)
   - Set password length (8-128)
   - Select character sets
   - View strength and entropy
   - Copy to clipboard

2. Validate Password
   - Check password strength
   - Calculate entropy
   - Analyze character composition

3. View Password History
   - View last 10 generated passwords
   - See generation timestamps
   - Review strength metrics

4. Exit

## 📂 File Structure
```
~/.termpassx/
├── termpassx.py         # Main script
├── password_history.txt # Password history file
└── requirements.txt     # Python dependencies
```

## 🔐 Security Features

- Uses Python's `secrets` module for cryptographic operations
- Enforces minimum password strength requirements
- Prevents excessive character repetition
- Calculates entropy for accurate strength measurement
- Secure clipboard handling through Termux:API

## 🔧 Termux:API Integration

### Clipboard Operations
- The tool uses `termux-clipboard-set` for secure clipboard operations
- Example usage in code:
```python
subprocess.run(['termux-clipboard-set'], input=password.encode(), check=True)
```

### Troubleshooting Termux:API
1. Check if Termux:API is installed:
```bash
pkg list-installed | grep termux-api
```

2. Verify Termux:API app is installed:
```bash
termux-clipboard-set "test"
```

3. Common issues:
   - "Command not found": Install termux-api package
   - "API not available": Install Termux:API app from F-Droid
   - Permission issues: Grant required permissions to Termux:API app

## 🤝 Contributing

Feel free to contribute to this project. Please follow these steps:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Mahedi Hasan Rafsun**
- Mobile: +8801306654467
- Email: developer.mahedihasanrafsun@gmail.com
- GitHub: [@mhrtuch240](https://github.com/mhrtuch240)

## 📝 Notes

- Keep your password history file secure
- Regular updates will be provided for security enhancements
- Report any bugs or security issues via email
- Make sure Termux:API permissions are properly configured

## ⚠️ Disclaimer

This tool is for legitimate password generation purposes only. The author is not responsible for any misuse or damage caused by this tool.

## 🔄 Version History

- v1.0.0 (2025-07-02)
  - Initial release
  - Added password history feature
  - Implemented Termux:API integration
  - Added multiple password generation

## 🐛 Known Issues

1. Emoji support may vary depending on terminal
2. Clipboard operations require Termux:API app
3. Some special characters may not display correctly in history file

## 💡 Tips

1. Keep Termux and Termux:API updated
2. Regularly check for tool updates
3. Back up your password history file
4. Use maximum entropy for sensitive passwords

---
Generated by: mhrtuch240
Last Updated: 2025-07-02 01:09:41 UTC
© 2025 Mahedi Hasan Rafsun. All Rights Reserved.
```
