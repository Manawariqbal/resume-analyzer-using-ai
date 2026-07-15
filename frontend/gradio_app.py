import gradio as gr
import requests

FASTAPI_URL = "http://localhost:8000"


def analyze_resume(pdf_file):

    if pdf_file is None:
        return {"error": "Please upload a resume"}

    with open(pdf_file, "rb") as f:

        response = requests.post(
            f"{FASTAPI_URL}/resume/upload",
            files={
                "file": f
            }
        )

    return response.json()


def match_resume_jd(pdf_file, job_description):

    if pdf_file is None:
        return {"error": "Please upload a resume"}

    with open(pdf_file, "rb") as f:

        response = requests.post(
            f"{FASTAPI_URL}/resume/match-jd",
            files={
                "file": f
            },
            data={
                "job_description": job_description
            }
        )

    return response.json()


with gr.Blocks(title="AI Resume Analyzer") as app:

    gr.Markdown("# AI Resume Analyzer")
    gr.Markdown(
        "Analyze resumes and compare them against job descriptions using AI."
    )

    # TAB 1
    with gr.Tab("Resume Analysis"):

        resume_file = gr.File(
            label="Upload Resume PDF"
        )

        analyze_btn = gr.Button(
            "Analyze Resume"
        )

        analysis_output = gr.JSON(
            label="Analysis Result"
        )

        analyze_btn.click(
            fn=analyze_resume,
            inputs=resume_file,
            outputs=analysis_output
        )

    # TAB 2
    with gr.Tab("JD Matching"):

        jd_resume = gr.File(
            label="Upload Resume PDF"
        )

        jd_text = gr.Textbox(
            label="Job Description",
            lines=12,
            placeholder="Paste job description here..."
        )

        match_btn = gr.Button(
            "Match Resume"
        )

        match_output = gr.JSON(
            label="Match Result"
        )

        match_btn.click(
            fn=match_resume_jd,
            inputs=[
                jd_resume,
                jd_text
            ],
            outputs=match_output
        )

app.launch()