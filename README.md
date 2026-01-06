# ai-resume-critique

Create a virtual environment (recommended)

bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Set up environment variables

bash
# Create a .env file
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
Get your FREE Groq API key

Visit console.groq.com

Sign up with Google/GitHub (free)

Navigate to "API Keys" in the sidebar

Click "Create API Key"

Copy your key and paste it in the .env file

🚀 Usage
Start the application

bash
streamlit run main.py
Open your browser

Navigate to http://localhost:8501

Using the application

text
1. 📤 Upload your resume (PDF or TXT)
2. 🎯 Enter your target job role
3. 🚀 Click "Analyze My Resume"
4. 📊 View detailed analysis report
5. 📥 Download your personalized feedback
📁 Project Structure
text
ai-resume-critique/
├── main.py                 # Main Streamlit application
├── pyproject.toml          # Python project dependencies
├── requirements.txt        # Required packages
├── .env                   # Environment variables (API keys)
├── .gitignore            # Git ignore file
├── README.md             # This documentation
└── screenshots/          # Screenshots for documentation
🎯 How It Works
1. File Processing
Upload PDF or text resumes

Automatic text extraction using PyPDF2

Content sanitization and formatting

2. AI Analysis
Sends content to Groq's Llama 3 model

Comprehensive prompt engineering for detailed feedback

Real-time analysis with progress tracking

3. Results Presentation
Structured report with multiple sections

Visual feedback with emojis and formatting

Downloadable text report

🔧 Configuration
Environment Variables
Create a .env file with:

env
GROQ_API_KEY=your_groq_api_key_here
Customization Options
You can modify:

AI Model: Change llama3-8b-8192 to other Groq models

Temperature: Adjust creativity in main.py

UI Colors: Modify CSS in the st.markdown section

Analysis Sections: Customize the prompt template

📈 Performance
Analysis Time: ~5-10 seconds per resume

File Size Limit: ~10MB (practical limit for resumes)

API Rate Limit: 30 requests/minute (Groq free tier)

Supported Formats: PDF, TXT

🤝 Contributing
We welcome contributions! Here's how:

Fork the repository

Create a feature branch

bash
git checkout -b feature/AmazingFeature
Commit your changes

bash
git commit -m 'Add some AmazingFeature'
Push to the branch

bash
git push origin feature/AmazingFeature
Open a Pull Request

Development Setup
bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests (add your test framework)
pytest tests/

# Format code
black main.py
🐛 Troubleshooting
Issue	Solution
Import errors	Run pip install -r requirements.txt
API key not found	Verify .env file exists and contains valid key
PDF extraction fails	Ensure PDF is not scanned/image-based
Slow analysis	Check internet connection; Groq servers may be busy
Rate limit exceeded	Wait 1 minute; free tier has 30 RPM limit
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Streamlit for the amazing web framework

Groq for providing free, fast LLM access

PyPDF2 for PDF processing

All contributors and users of this project

📞 Support
If you encounter any problems or have questions:

Check the Issues page

Search existing issues for similar problems

Create a new issue with detailed information

Include: Error messages, steps to reproduce, and screenshots



