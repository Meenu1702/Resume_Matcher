# Resume Matcher

## Overview
Resume Matcher is a web-based application designed to analyze resumes and match them with job descriptions. It leverages **Streamlit** for the frontend and **FastAPI** for the backend, integrating various NLP techniques to enhance resume analysis.

## Features
- **Upload Resume**: Users can upload their resumes in PDF or DOCX format.
- **Job Description Matching**: Compares the resume against a given job description.
- **Skill Extraction**: Extracts key skills and highlights missing ones.
- **Scoring System**: Assigns a similarity score between the resume and job description.
- **FastAPI Backend**: Handles API requests and performs processing.
- **Streamlit Frontend**: Provides an interactive and user-friendly UI.

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Libraries**: NLTK, Spacy, scikit-learn, pandas, PyPDF2
- **Deployment**: Can be hosted on platforms like AWS, Render, or Heroku

## Installation
### Prerequisites
Ensure you have Python installed (3.10 or later).

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/resume-matcher.git
cd resume-matcher
```

### Step 2: Set Up Virtual Environment
```bash
python -m venv venv
```
Activate the virtual environment:
- **Windows (PowerShell)**:
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **Windows (Command Prompt)**:
  ```cmd
  venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
### Running FastAPI Backend
```bash
uvicorn backend.main:app --reload
```
The API will be available at: `http://127.0.0.1:8000`

### Running Streamlit Frontend
```bash
streamlit run frontend/app.py
```

## API Endpoints
| Method | Endpoint          | Description                  |
|--------|------------------|------------------------------|
| POST   | `/match`         | Matches a resume with a job description |
| POST   | `/extract-skills` | Extracts skills from a resume |

## Contributing
Feel free to fork this project and submit pull requests with improvements.


