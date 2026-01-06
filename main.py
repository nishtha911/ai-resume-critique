import streamlit as st
import PyPDF2
import io
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critique", page_icon="📃", layout="centered")

st.title("AI Resume Critique")
st.markdown("Upload your Resume and get AI-powered feedback")

# Get Groq API key - FREE from https://console.groq.com
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

uploaded_file = st.file_uploader("Upload your Resume (.pdf or .txt)", type=["pdf", "txt"])
job_role = st.text_input("Enter your target job role: ")

analyze = st.button("Analyze Resume")

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

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)
        
        if not file_content.strip():
            st.error("File does not have any content!")
            st.stop()
            
        # Limit content to avoid token issues
        file_content_limited = file_content[:3000]
        
        prompt = f"""You are an expert resume reviewer with years of experience in HR and recruitment.

Please analyze this resume and provide constructive feedback.
Focus on the following aspects:
1. Content clarity and impact
2. Skills Presentation
3. Experience Description
4. Specific improvements for {job_role if job_role else 'general job applications'}

Resume content:
{file_content_limited}

Please provide your analysis in a clear structured format with specific recommendations and actionable tips."""
        
        if not GROQ_API_KEY:
            st.error("⚠️ Groq API Key is missing!")
            st.markdown("""
            **How to get a FREE API Key:**
            1. Go to: https://console.groq.com
            2. Sign up (free with Google/GitHub)
            3. Click "API Keys" in left sidebar
            4. Create a new API key
            5. Copy the key
            6. Create a `.env` file in your project folder and add:
            ```
            GROQ_API_KEY=your_key_here
            ```
            """)
            st.stop()
        
        # Call Groq API
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "openai/gpt-oss-120b",  # Free model, very fast
            "messages": [
                {
                    "role": "system",
                    "content": "You are an expert resume reviewer with years of experience in HR and recruitment. Provide clear, actionable feedback."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7,
            "max_tokens": 1500,
            "top_p": 1,
            "stream": False
        }
        
        with st.spinner("🤖 Analyzing your resume..."):
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=payload
            )
        
        if response.status_code == 200:
            result = response.json()
            analysis = result['choices'][0]['message']['content']
            
            st.markdown("### 📋 Analysis Results")
            st.markdown(analysis)
            
            # Add some statistics
            st.markdown("---")
            st.caption(f"Analysis completed using Groq's Llama model")
            
        elif response.status_code == 401:
            st.error("Invalid API key. Please check your Groq API key.")
        elif response.status_code == 429:
            st.error("Rate limit exceeded. Please try again in a moment.")
        else:
            st.error(f"API Error: {response.status_code}")
            st.text(f"Response: {response.text}")
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Make sure you have a stable internet connection.")