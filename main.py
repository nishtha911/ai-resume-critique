import streamlit as st
import PyPDF2
import io
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Resume Critique",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Title styling */
    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-size: 3rem !important;
        font-weight: 800 !important;
        margin-bottom: 0.5rem !important;
        background: linear-gradient(90deg, #1E3A8A, #3B82F6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .subtitle {
        text-align: center;
        color: #6B7280;
        font-size: 1.2rem !important;
        margin-bottom: 2.5rem !important;
    }
    
    /* Card styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #F3F4F6;
        border-radius: 10px 10px 0px 0px;
        gap: 1rem;
        padding-top: 10px;
        padding-bottom: 10px;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #3B82F6 !important;
        color: white !important;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        height: 50px;
        font-weight: 600;
        font-size: 1.1rem;
        background: linear-gradient(90deg, #1E3A8A, #3B82F6);
        color: white;
        border: none;
        border-radius: 12px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(37, 99, 235, 0.3);
        background: linear-gradient(90deg, #1E40AF, #2563EB);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* File uploader styling */
    .uploadedFile {
        border: 2px dashed #3B82F6 !important;
        border-radius: 12px !important;
        padding: 2rem !important;
        background-color: #F0F9FF !important;
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        border: 2px solid #E5E7EB;
        border-radius: 10px;
        padding: 12px;
        font-size: 1rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #3B82F6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
    }
    
    /* Success message styling */
    .success-message {
        background: linear-gradient(90deg, #10B981, #34D399);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    /* Analysis results styling */
    .analysis-box {
        background: linear-gradient(135deg, #F9FAFB 0%, #F3F4F6 100%);
        border-left: 5px solid #3B82F6;
        padding: 2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    
    .section-title {
        color: #1F2937;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        margin-top: 1.5rem !important;
        margin-bottom: 1rem !important;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .section-title::before {
        content: "📌";
        font-size: 1.2rem;
    }
    
    /* Progress bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #3B82F6, #60A5FA);
    }
    
    /* Metrics styling */
    .metric-box {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        text-align: center;
        margin: 0.5rem;
    }
    
    .metric-value {
        font-size: 2rem !important;
        font-weight: 800 !important;
        color: #1E3A8A !important;
        margin-bottom: 0.5rem !important;
    }
    
    .metric-label {
        color: #6B7280 !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid #E5E7EB;
        color: #6B7280;
        font-size: 0.9rem;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem !important;
        }
        .subtitle {
            font-size: 1rem !important;
        }
    }
    
    /* Custom badge */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        background: #DBEAFE;
        color: #1E40AF;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.25rem;
    }
    
    /* Spinner animation */
    .stSpinner > div {
        border-color: #3B82F6 !important;
        border-right-color: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<h1 class="main-title">📄 AI Resume Critique Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Get professional, AI-powered feedback to land your dream job</p>', unsafe_allow_html=True)

# Initialize session state
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None

# Create two columns for layout
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📤 Upload Your Resume")
    
    # File upload section
    uploaded_file = st.file_uploader(
        "Drag and drop or click to upload",
        type=["pdf", "txt"],
        help="Supported formats: PDF, Text",
        label_visibility="collapsed"
    )
    
    if uploaded_file:
        file_details = {
            "Filename": uploaded_file.name,
            "File size": f"{uploaded_file.size / 1024:.1f} KB",
            "File type": uploaded_file.type
        }
        
        st.markdown("""
        <div style='background-color: #F0F9FF; padding: 1.5rem; border-radius: 12px; border: 2px solid #3B82F6; margin: 1rem 0;'>
            <div style='display: flex; align-items: center; gap: 1rem;'>
                <div style='font-size: 2rem;'>📄</div>
                <div>
                    <h4 style='margin: 0; color: #1E3A8A;'>{filename}</h4>
                    <p style='margin: 0.25rem 0; color: #6B7280; font-size: 0.9rem;'>
                        📏 Size: {size} • 📊 Type: {type}
                    </p>
                </div>
            </div>
        </div>
        """.format(
            filename=uploaded_file.name,
            size=file_details["File size"],
            type=file_details["File type"].split('/')[-1].upper()
        ), unsafe_allow_html=True)
    
    # Job role input
    st.markdown("### 🎯 Target Position")
    job_role = st.text_input(
        "What job are you applying for?",
        placeholder="e.g., Senior Software Engineer, Marketing Manager",
        label_visibility="collapsed"
    )
    
    # Analysis button
    st.markdown("<br>", unsafe_allow_html=True)
    analyze = st.button(
        "🚀 Analyze My Resume",
        use_container_width=True,
        type="primary"
    )

with col2:
    if uploaded_file and job_role:
        st.markdown("### 📊 Quick Preview")
        
        # Display some stats
        col_stat1, col_stat2, col_stat3 = st.columns(3)
        
        with col_stat1:
            st.markdown("""
            <div class="metric-box">
                <div class="metric-value">🎯</div>
                <div class="metric-label">Position</div>
                <div style='font-weight: 600; color: #1F2937;'>{}</div>
            </div>
            """.format(job_role[:15] + "..." if len(job_role) > 15 else job_role), unsafe_allow_html=True)
        
        with col_stat2:
            st.markdown("""
            <div class="metric-box">
                <div class="metric-value">📄</div>
                <div class="metric-label">Format</div>
                <div style='font-weight: 600; color: #1F2937;'>{}</div>
            </div>
            """.format(uploaded_file.type.split('/')[-1].upper()), unsafe_allow_html=True)
        
        with col_stat3:
            st.markdown("""
            <div class="metric-box">
                <div class="metric-value">⚡</div>
                <div class="metric-label">Ready</div>
                <div style='font-weight: 600; color: #10B981;'>Analyze Now</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%); padding: 2rem; border-radius: 12px; margin-top: 2rem;'>
        <h4 style='color: #1E3A8A; margin-top: 0;'>✨ What You'll Get:</h4>
        <ul style='color: #4B5563;'>
            <li>📝 <strong>Content Analysis</strong> - Clarity & impact assessment</li>
            <li>🎯 <strong>Skills Evaluation</strong> - Presentation & relevance</li>
            <li>💼 <strong>Experience Review</strong> - Achievements & formatting</li>
            <li>🚀 <strong>Custom Recommendations</strong> - Tailored for your target role</li>
            <li>📈 <strong>Actionable Tips</strong> - Specific improvements</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# File extraction functions
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + '\n'
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

# Main analysis logic
if analyze and uploaded_file:
    try:
        # Show progress
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("📥 Reading your resume...")
        progress_bar.progress(25)
        
        file_content = extract_text_from_file(uploaded_file)
        
        if not file_content.strip():
            st.error("❌ File does not have any readable content!")
            st.stop()
        
        status_text.text("🔍 Processing content...")
        progress_bar.progress(50)
        
        # Get Groq API key
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        
        if not GROQ_API_KEY:
            st.error("⚠️ API Key Missing!")
            st.markdown("""
            <div style='background-color: #FEF2F2; padding: 1.5rem; border-radius: 12px; border-left: 5px solid #DC2626;'>
                <h4 style='color: #DC2626; margin-top: 0;'>Setup Required:</h4>
                <ol style='color: #4B5563;'>
                    <li>Get a <strong>FREE API key</strong> from <a href='https://console.groq.com' target='_blank'>Groq Console</a></li>
                    <li>Create a <code>.env</code> file in your project folder</li>
                    <li>Add this line: <code>GROQ_API_KEY=your_key_here</code></li>
                </ol>
                <p style='color: #6B7280; font-size: 0.9rem; margin-top: 1rem;'>
                    Don't worry, it's completely free and takes only 2 minutes!
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.stop()
        
        status_text.text("🤖 AI is analyzing your resume...")
        progress_bar.progress(75)
        
        # Prepare the prompt
        prompt = f"""You are an expert resume reviewer and career coach with 15+ years of experience in HR and recruitment at top tech companies.

RESUME ANALYSIS REQUEST:
Target Position: {job_role}

RESUME CONTENT:
{file_content[:2500]}

PLEASE PROVIDE A COMPREHENSIVE ANALYSIS WITH THESE SECTIONS:

1. **EXECUTIVE SUMMARY**
   - Overall impression
   - Strengths highlighted
   - Major areas for improvement

2. **CONTENT ASSESSMENT** (Rate each 1-5 ⭐)
   - Clarity & Readability
   - Impact & Achievements
   - Relevance to {job_role}

3. **SKILLS ANALYSIS**
   - Technical skills presentation
   - Soft skills visibility
   - Skills gap analysis for {job_role}

4. **EXPERIENCE REVIEW**
   - STAR method usage (Situation, Task, Action, Result)
   - Quantifiable achievements
   - Career progression clarity

5. **ACTIONABLE RECOMMENDATIONS**
   - 3 immediate improvements
   - Keywords to add for {job_role}
   - Formatting suggestions
   - Power verbs to incorporate

6. **FINAL SCORE & VERDICT**
   - Overall score (1-10)
   - Readiness for {job_role}
   - Next steps

Format with clear headers, bullet points, and use emojis for readability. Be constructive, specific, and encouraging."""

        # Call Groq API
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "openai/gpt-oss-120b",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a world-class resume expert who provides detailed, actionable, and encouraging feedback. Format responses beautifully with clear sections, emojis, and bullet points."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7,
            "max_tokens": 2000,
            "top_p": 1,
            "stream": False
        }
        
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )
        
        status_text.text("📋 Preparing your report...")
        progress_bar.progress(95)
        
        if response.status_code == 200:
            result = response.json()
            analysis = result['choices'][0]['message']['content']
            st.session_state.analysis_result = analysis
            
            progress_bar.progress(100)
            status_text.empty()
            progress_bar.empty()
            
            # Success message
            st.markdown("""
            <div class="success-message">
                <h3 style='margin: 0; color: white;'>✅ Analysis Complete!</h3>
                <p style='margin: 0.5rem 0 0 0; color: #D1FAE5;'>Your personalized resume critique is ready below.</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display results in a nice container
            st.markdown("### 📊 Detailed Analysis Report")
            st.markdown('<div class="analysis-box">', unsafe_allow_html=True)
            st.markdown(analysis)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Add download button for the analysis
            st.download_button(
                label="📥 Download Analysis Report",
                data=analysis,
                file_name=f"resume_analysis_{job_role.replace(' ', '_')}.txt",
                mime="text/plain",
                use_container_width=True
            )
            
        else:
            progress_bar.empty()
            status_text.empty()
            st.error(f"API Error {response.status_code}")
            
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")

# Footer
st.markdown("""
<div class="footer">
    <p>Built with ❤️ using Streamlit & Groq AI by @nishtha911 • Resume Critique Pro v1.0</p>
    <p style='font-size: 0.8rem; color: #9CA3AF;'>
        Your resume data is processed securely and not stored.
    </p>
</div>
""", unsafe_allow_html=True)