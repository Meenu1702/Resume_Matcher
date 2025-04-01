import streamlit as st
import requests

# Custom CSS for Background, Fonts, Borders, and Buttons
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ADD8E6;  /* Light blue background */
    }
    h1 {
        font-family: 'Georgia', serif;  /* Custom font for title */
        font-size: 42px;
        color: #FF4081;  /* Title color */
        text-align: center;
    }
    .stButton>button {
        background-color: #90EE90 !important;  /* Light green button */
        color: black !important;
        font-size: 18px;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stTextArea>textarea, .stFileUploader {
        border: 3px solid #FF4081 !important;  /* Pink border */
        border-radius: 10px !important;
        padding: 10px !important;
        font-size: 16px;
    }
    .footer {
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        margin-top: 50px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with custom font
st.markdown("<h1>📝 RESUME MATCHER</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")
job_desc = st.text_area("Job Description (Paste Here)")

if st.button("Analyze Resume & Match"):
    if uploaded_file and job_desc:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:8000/analyze/", files=files, data={"job_desc": job_desc})

        if response.status_code == 200:
            result = response.json()
            # New, fun output format
            st.subheader("🔍 Resume Analysis Results")
            st.write(f"**Match Score**: {result['match_score']}%")
            st.write("### Extracted Skills & Insights:")
            st.write(f"✨ **Skills Found**: {', '.join(result['insights']['skills'])}")
        else:
            st.error("🚨 Error during analysis. Please try again!")
    else:
        st.warning("⚠️ Please upload a resume and provide a job description.")

# Footer with creator's name
st.markdown('<div class="footer">🚀 Made by @meenamehaira@gmail.com</div>', unsafe_allow_html=True)
