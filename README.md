# 🚀 AI-Powered Resume Screener API

A production-ready **FastAPI** application that accepts a job description (JD) and a resume (PDF/Text), uses **Generative AI (Gemini)** to return a detailed ATS compatibility score, and provides targeted feedback.

---

## ✨ Features

- 📄 **Resume Scoring**: Analyze resumes against job descriptions for ATS compatibility.
- 🤖 **AI-Powered Feedback**: Get detailed insights, missing keywords, and summaries using Google Gemini.
- ⚡ **High Performance**: Built with FastAPI for speed and efficiency.
- 🐳 **Dockerized**: Ready for containerized deployment.
- 🖥️ **Simple Frontend**: Includes a lightweight HTML/JS frontend for easy testing.

## 🛠️ Tech Stack

| Component      | Technology                                                                                                | Description                             |
| :------------- | :-------------------------------------------------------------------------------------------------------- | :-------------------------------------- |
| **Framework**  | ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)                           | High-performance web framework          |
| **Language**   | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)              | Core programming language               |
| **AI Model**   | ![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=flat&logo=googlebard&logoColor=white) | Generative AI for analysis              |
| **Database**   | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white)  | Persistent storage (SQLAlchemy ORM)     |
| **Validation** | Pydantic                                                                                                  | Data validation and settings management |
| **Deployment** | Docker                                                                                                    | Containerization                        |

## 🔌 API Endpoints

| Method | Endpoint                      | Description                        | Request Body                                            |
| :----- | :---------------------------- | :--------------------------------- | :------------------------------------------------------ |
| `GET`  | `/health`                     | Check API health status            | N/A                                                     |
| `POST` | `/api/v1/score`               | Submit JD and Resume for analysis  | `{"job_description": "...", "candidate_resume": "..."}` |
| `GET`  | `/api/v1/feedback/{score_id}` | Retrieve detailed analysis results | N/A                                                     |

## ⚙️ Setup & Installation

### Prerequisites

- 🐍 Python 3.9+
- 🔑 Google Gemini API Key
- 🐳 Docker (Optional)

### 🚀 Quick Start (Local)

1.  **Clone the repository**

    ```bash
    git clone <repository-url>
    cd AI-Powered-Resume
    ```

2.  **Create a virtual environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Environment Variables**
    Create a `.env` file or export them directly:

    ```bash
    export GEMINI_API_KEY=your_actual_api_key_here
    # Database defaults to SQLite (test.db) if not provided
    # export DATABASE_URL=postgresql://user:password@localhost/dbname
    ```

5.  **Run the Backend**
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will be available at `http://localhost:8000`.

### 🖥️ Using the Frontend

1.  Ensure the backend is running.
2.  Open `frontend/index.html` in your web browser.
3.  Enter a **Job Description** and **Resume Text**.
4.  Click **"Analyze Resume"**.

### 🐳 Running with Docker

1.  **Build the image**

    ```bash
    docker build -t resume-screener .
    ```

2.  **Run the container**
    ```bash
    docker run -p 8000:8000 -e GEMINI_API_KEY=your_key resume-screener
    ```

## 📚 Documentation

Once the server is running, you can access the interactive API documentation:

- **Swagger UI**: [`http://localhost:8000/docs`](http://localhost:8000/docs)
- **ReDoc**: [`http://localhost:8000/redoc`](http://localhost:8000/redoc)

## 🤝 Git Workflow

We follow the **Feature Branch Workflow**:

| Branch      | Purpose                                         |
| :---------- | :---------------------------------------------- |
| `main`      | 🛡️ Production ready code.                       |
| `develop`   | 🚧 Integration branch for testing.              |
| `feature/*` | ✨ Feature branches (e.g., `feature/add-auth`). |

Happy Coading❤️
