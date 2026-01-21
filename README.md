# 🔗 Linkfy

A simple and efficient CLI tool to shorten URLs with local SQLite history tracking.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 🚀 **Fast URL shortening** using TinyURL API
- 💾 **Local history** stored in SQLite database
- 🏷️ **Custom aliases** for easy link identification
- 📋 **Clipboard support** (optional)
- 📊 **History management** with search capabilities
- 🎯 **Simple CLI interface**

## 📦 Installation

### From source

```bash
# Clone the repository
git clone https://github.com/matheusc457/linkfy.git
cd linkfy

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install linkfy
pip install -e .
```

## 🚀 Usage

### Basic usage

```bash
# Shorten a URL
linkfy https://www.example.com

# Shorten with custom alias
linkfy https://github.com/matheusc457 --alias myrepo

# Copy shortened URL to clipboard
linkfy https://example.com --copy
```

### View history

```bash
# Show all shortened URLs
linkfy --history

# Show last shortened URL
linkfy --last

# Limit history results
linkfy --history --limit 5
```

### Help

```bash
linkfy --help
```

## 📋 Examples

```bash
# Shorten a URL
$ linkfy https://www.google.com
Shortening URL: https://www.google.com

✓ Shortened URL: https://tinyurl.com/abc123

# With alias
$ linkfy https://github.com --alias mygithub
Shortening URL: https://github.com

✓ Shortened URL: https://tinyurl.com/xyz789
  Alias: mygithub

# View history
$ linkfy --history

ID    Original URL                             Shortened URL                  Alias           Date                
--------------------------------------------------------------------------------------------------------------
2     https://github.com                       https://tinyurl.com/xyz789     mygithub        2026-01-21 08:15:30
1     https://www.google.com                   https://tinyurl.com/abc123     -               2026-01-21 08:12:45
```

## 🛠️ Requirements

- Python 3.6+
- requests
- pyperclip (optional, for clipboard support)

## 📁 Project Structure

```
linkfy/
├── linkfy/
│   ├── __init__.py
│   ├── __main__.py
│   ├── main.py          # CLI interface
│   ├── database.py      # SQLite database handler
│   └── shortener.py     # URL shortening logic
├── requirements.txt
├── setup.py
├── README.md
└── LICENSE
```

## 🗄️ Database Schema

The SQLite database stores:
- `id`: Auto-incrementing primary key
- `original_url`: Original long URL
- `shortened_url`: Shortened URL from TinyURL
- `alias`: Optional custom alias
- `created_at`: Timestamp of creation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Matheus Campos**
- GitHub: [@matheusc457](https://github.com/matheusc457)
- Email: mclealpvp10@gmail.com

## 🙏 Acknowledgments

- [TinyURL](https://tinyurl.com/) for the URL shortening API
- Built with ❤️ using Python

## 📮 Support

If you have any questions or issues, please [open an issue](https://github.com/matheusc457/linkfy/issues).

---

Made with ❤️ by [Matheus Campos](https://github.com/matheusc457)
