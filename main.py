import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title= "AI Resume Critique", page_icon="📃", layout="centered")

st.title("AI Resume Critique")
st.markdown("Upload your Resume and get AI-powered feedback")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader("Upload you Resume (.pdf or .txt)", type=["pdf", "txt"])
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
            
        prompt = f"""Please analyze this reume and provide constructive feedback
        """
            
