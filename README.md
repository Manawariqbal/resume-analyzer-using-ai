# AI Resume Analyzer

AI-powered Resume Analyzer built using **FastAPI**, **LangChain**, and **Groq LLMs**. The application allows users to upload resumes, receive ATS-style analysis, and compare resumes against job descriptions to identify skill gaps and improvement opportunities.

## Features

* Upload PDF resumes
* Extract text from resumes
* ATS-style resume analysis
* Skill extraction and evaluation
* Resume strengths and weaknesses
* Improvement recommendations
* Resume vs Job Description matching
* Structured JSON responses using Pydantic
* Groq LLM integration through LangChain

---

## Tech Stack

### Backend

* Python
* FastAPI
* Pydantic
* LangChain
* Groq

### PDF Processing

* PyMuPDF (fitz)

### Frontend

* Streamlit

---

## Project Structure

```text
resume-analyzer/

├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   └── resume.py
│   │
│   ├── services/
│   │   ├── file_service.py
│   │   ├── pdf_service.py
│   │   ├── ai_service.py
│   │   └── jd_service.py
│   │
│   ├── schemas/
│   │   ├── resume_schema.py
│   │   └── jd_schema.py
│   │
│   ├── models/
│   │
│   └── database/
│
├── frontend/
│   └── app.py
│
├── uploads/
│
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>

cd resume-analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Running FastAPI

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Running Streamlit Frontend

```bash
streamlit run frontend/app.py
```

---

## API Endpoints

### Upload Resume

```http
POST /resume/upload
```

Returns:

* ATS Score
* Strengths
* Weaknesses
* Missing Skills
* Suggestions

---

### Match Resume with Job Description

```http
POST /resume/match-jd
```

Returns:

* Match Percentage
* Strengths
* Missing Skills
* Recommendations

---

## Sample Response

```json
{
  "ats_score": 84,
  "strengths": [
    "Python",
    "FastAPI",
    "PostgreSQL"
  ],
  "weaknesses": [
    "Missing Docker experience"
  ],
  "missing_skills": [
    "Redis",
    "Kubernetes"
  ],
  "suggestions": [
    "Add containerized backend projects"
  ]
}
```

---

## Future Enhancements

* Authentication (JWT)
* PostgreSQL persistence
* Docker deployment
* Resume history
* Multi-file support
* Vector database integration
* RAG-based resume insights
* Multi-LLM support (Groq, OpenAI, Gemini, Anthropic)

---

## Author

Md Manawar Iqbal

Python Backend Engineer | AI Engineer
