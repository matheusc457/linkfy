# 🔗 Linkfy

[![CI/CD Pipeline](https://github.com/matheusc457/linkfy/actions/workflows/ci.yml/badge.svg)](https://github.com/matheusc457/linkfy/actions/workflows/ci.yml)
![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A simple and efficient CLI tool to shorten URLs with local SQLite history tracking.

## ✨ Features

- 🚀 **Fast URL shortening** using TinyURL API
- 💾 **Local history** stored in SQLite database
- 🏷️ **Custom aliases** for easy link identification
- 📋 **Clipboard support** (optional)
- 📊 **History management** with search capabilities
- 🎯 **Simple CLI interface**
- ✅ **Fully tested** with automated CI/CD

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

# With clipboard copy
$ linkfy https://python.org --copy
Shortening URL: https://python.org

✓ Shortened URL: https://tinyurl.com/def456
  (Copied to clipboard)

# View history
$ linkfy --history

ID    Original URL                             Shortened URL                  Alias           Date                
--------------------------------------------------------------------------------------------------------------
3     https://python.org                       https://tinyurl.com/def456     -               2026-01-21 08:30:12
2     https://github.com                       https://tinyurl.com/xyz789     mygithub        2026-01-21 08:15:30
1     https://www.google.com                   https://tinyurl.com/abc123     -               2026-01-21 08:12:45

# View last shortened URL
$ linkfy --last

Last shortened URL:
  Original:  https://python.org
  Shortened: https://tinyurl.com/def456
  Date:      2026-01-21 08:30:12
```

## 🛠️ Requirements

- Python 3.9+
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
├── tests/
│   ├── test_database.py
│   └── test_shortener.py
├── .github/
│   └── workflows/
│       └── ci.yml       # CI/CD pipeline
├── requirements.txt
├── requirements-dev.txt
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

## 🧪 Development

### Running tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ -v --cov=linkfy --cov-report=term-missing

# Check code formatting
black --check linkfy/

# Format code
black linkfy/ tests/

# Lint code
flake8 linkfy/
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to:
- Write tests for new features
- Follow the existing code style (use `black` for formatting)
- Update documentation as needed

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
