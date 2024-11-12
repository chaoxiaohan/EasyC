# EasyC 🚀

<div align="center">

English | [简体中文](https://github.com/ophiraShen/EasyC/blob/main/README_CN.MD)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-required-blue.svg)](https://www.docker.com/)

An intuitive, AI-powered platform designed to make learning C programming accessible and engaging for complete beginners.
</div>

## 🌟 Features

### 1. Code Compilation & Execution
- Real-time C code compilation
- Interactive code execution
- Comprehensive error handling
- Program input/output support

### 2. AI-Powered Analysis
- Intelligent code review
- Optimization suggestions
- Error diagnosis
- Learning recommendations

### 3. User Interface
- Clean and intuitive design
- Real-time feedback
- Responsive layout
- Syntax highlighting

## 🔧 System Architecture

```
EasyC
├── Frontend (Gradio)
│   ├── Code Editor
│   ├── Settings Panel
│   └── Output Display
│
├── Backend Services
│   ├── Compiler Service
│   └── AI Feedback Service
│
└── Utils
    ├── Logger
    └── Path Management
```

## 🚀 Quick Start

### Using Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/ophiraShen/EasyC.git

# Start with Docker Compose
docker-compose up --build
```

### Manual Installation
```bash
# Clone the repository
git clone https://github.com/ophiraShen/EasyC.git

# Install dependencies
pip install -r requirements.txt

# Start the application
python src/main.py
```

## 💻 Requirements

### System Requirements
- Python 3.10+
- GCC Compiler
- Docker (optional)

### Dependencies
- Gradio 5.4.0
- Python-dotenv 1.0.1
- Loguru 0.7.2
- Additional dependencies in `requirements.txt`

## 🛠️ Development

### Project Structure
```
src/
├── backend/               # Backend services
│   ├── ai/               # AI analysis
│   └── compiler/         # Code compilation
├── frontend/             # UI components
├── utils/               # Utilities
└── main.py              # Entry point
```

### Key Components
1. **Frontend Module**
   - Gradio-based UI
   - Responsive design
   - Theme management

2. **Backend Module**
   - Code compilation
   - AI analysis
   - Error handling

3. **Utils Module**
   - Logging system
   - Path management
   - Common utilities

## 📝 Documentation

Detailed documentation for each module:
- [Frontend Documentation](src/frontend/functional_docs/README_frontend.md)
- [Backend Documentation](src/backend/functional_docs/README_backend.md)
- [Utils Documentation](src/utils/functional_docs/README_utils.md)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md).

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🔒 Security

- Secure code execution environment
- API key protection
- Regular security updates
- Resource usage limits

## 📈 Future Plans

1. **Feature Expansion**
   - Support for more programming languages
   - Advanced code analysis
   - Learning resource integration

2. **Technical Improvements**
   - Performance optimization
   - Enhanced AI capabilities
   - Mobile responsiveness

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- GCC team for the C compiler
- Docker for containerization
- All our contributors and supporters

## 📬 Contact

Project Link: [https://github.com/ophiraShen/EasyC](https://github.com/ophiraShen/EasyC)

---

<p align="center">Made with ❤️ for aspiring C programmers</p>