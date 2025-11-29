# AI-Powered Resume Screener API

A production-ready FastAPI application that accepts a job description (JD) and a resume (PDF/Text) and returns a detailed ATS compatibility score and targeted feedback using Generative AI.

## Features

- **Score Resume**: POST `/api/v1/score` - Accepts JD and Resume, returns an analysis ID.
- **Get Feedback**: GET `/api/v1/feedback/{score_id}` - Retrieves detailed analysis.
- **Health Check**: GET `/health` - API health status.
- **Frontend**: Simple HTML interface for testing.

## Tech Stack

- **Framework**: FastAPI
- **Validation**: Pydantic
- **Database**: PostgreSQL (SQLAlchemy ORM) or SQLite (default for testing)
- **AI**: Google Gemini API
- **Deployment**: Docker

## Setup

### Prerequisites

- Python 3.9+
- Google Gemini API Key
- (Optional) Docker
- (Optional) PostgreSQL

### Quick Start (Local)

1.  **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd AI-Powered-Resume
    ```

2.  **Create a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Environment Variables**:
    Create a `.env` file or export them directly:

    ```bash
    export GEMINI_API_KEY=your_actual_api_key_here
    # Database defaults to SQLite if not provided
    # export DATABASE_URL=postgresql://user:password@localhost/dbname
    ```

5.  **Run the Backend**:
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will be available at `http://localhost:8000`.

### Using the Frontend

1.  Ensure the backend is running.
2.  Open `frontend/index.html` in your web browser.
3.  Enter a Job Description and Resume text.
4.  Click "Analyze Resume".

### Running with Docker

1.  Build the image:

    ```bash
    docker build -t resume-screener .
    ```

2.  Run the container:
    ```bash
    docker run -p 8000:8000 -e GEMINI_API_KEY=your_key resume-screener
    ```

## API Documentation

Once the server is running, access the interactive API docs at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Troubleshooting

- **AI Error / 0 Score**: Ensure your `GEMINI_API_KEY` is valid and has access to the `gemini-1.5-flash` model.
- **Database Error**: If using PostgreSQL, ensure the database server is running and the URL is correct. For SQLite, ensure the app has write permissions to the directory.

## Git Workflow

We use the Feature Branch Workflow:

- `main`: Production ready.
- `develop`: Integration branch.
- `feature/*`: Feature branches.

## License

MIT
