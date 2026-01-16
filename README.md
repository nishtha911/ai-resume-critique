# AI Resume Critique Pro

<div align="center">

**An intelligent AI-powered resume analysis tool that provides comprehensive feedback and improvement suggestions**

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)](https://ai-resume-critique-nishtha911.streamlit.app/)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)

</div>

---

## 📋 Overview

AI Resume Critique Pro is a modern web application that leverages cutting-edge AI technology to analyze resumes and provide actionable feedback. Upload your resume in PDF format and receive detailed critiques, suggestions for improvement, and insights on how to make your resume more competitive.

Whether you're a job seeker looking to optimize your application materials or an HR professional reviewing candidates, this tool provides intelligent analysis to help you succeed.

## ✨ Features

- 📄 **PDF Resume Upload** - Easy drag-and-drop interface for resume files
- 🤖 **AI-Powered Analysis** - Uses advanced language models for intelligent critique
- 💬 **Detailed Feedback** - Comprehensive analysis with specific suggestions
- 🎯 **Resume Optimization** - Tips for improving content, structure, and formatting
- 📊 **Interactive Interface** - Beautiful, user-friendly Streamlit application
- ⚡ **Fast Processing** - Quick turnaround on resume analysis

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nishtha911/ai-resume-critique.git
   cd ai-resume-critique
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

The app will open in your browser at `http://localhost:8501`

## 📦 Dependencies

- **streamlit** - Web application framework
- **PyPDF2** - PDF file parsing and text extraction
- **python-dotenv** - Environment variable management
- **requests** - HTTP library for API calls
- **google-generativeai** - AI model integration (optional)

## 🎯 Usage

1. Open the application in your web browser
2. Click the **"Upload Resume"** button or drag-and-drop a PDF file
3. Wait for the AI to analyze your resume
4. Review the detailed critique and suggestions
5. Implement the recommendations to improve your resume

## 📸 Screenshots

### Home Page
![Home Page](home%20page.png)

### Resume Upload
![Resume Upload](add%20resume.png)

### Analysis Results
![Analysis Results1](analysis%20res1.png)
![Analysis Results2](analysis%20res2.png)

## 🏗️ Project Structure

```
ai-resume-critique/
├── main.py              # Main Streamlit application
├── requirements.txt     # Project dependencies
├── pyproject.toml       # Project metadata
├── README.md           # This file
└── .env.example        # Example environment variables
```

## 🔧 Configuration

### Environment Variables

Configure the following in your `.env` file:

- `GROQ_API_KEY` - Your Groq API key for AI analysis
- Additional API keys as needed for your AI model provider

## 🎨 Features in Detail

### Resume Upload
- Supports PDF format
- Handles multi-page resumes
- Extracts text automatically for analysis

### AI Analysis
- Grammar and spelling check
- Content relevance analysis
- Formatting and structure evaluation
- Keywords and ATS optimization suggestions
- Overall resume score and rating

### User Interface
- Modern, responsive design
- Intuitive navigation with tabs
- Real-time feedback
- Mobile-friendly layout

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Groq API](https://groq.com/)
- PDF processing with [PyPDF2](https://github.com/py-pdf/PyPDF2)

## 📧 Support

Have questions or need assistance? 

- Open an [Issue](https://github.com/nishtha911/ai-resume-critique/issues)
- Check existing [Discussions](https://github.com/nishtha911/ai-resume-critique/discussions)

## 🗺️ Roadmap

- [ ] Support for additional file formats (DOCX, TXT)
- [ ] Resume templates and examples
- [ ] Export feedback as PDF report
- [ ] Batch resume analysis
- [ ] Resume comparison features
- [ ] Industry-specific analysis
- [ ] Real-time typing suggestions

---

<div align="center">

**Made with ❤️ by nishtha911 for job seekers and HR professionals**

</div>
