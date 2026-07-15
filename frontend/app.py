import streamlit as st
import requests

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    files = {
        "file": uploaded_file
    }

    response = requests.post(
        "http://localhost:8000/resume/upload",
        files=files
    )

    st.json(response.json())