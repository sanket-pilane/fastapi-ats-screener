# AI-Powered Resume Screener API

A production-ready FastAPI application that accepts a job description (JD) and a resume (PDF/Text) and returns a detailed ATS compatibility score and targeted feedback using Generative AI.

## Features

- **Score Resume**: POST `/api/v1/score` - Accepts JD and Resume, returns an analysis ID.
- **Get Feedback**: GET `/api/v1/feedback/{score_id}` - Retrieves detailed analysis.
- **Health Check**: GET `/health` - API health status.

## Tech Stack

- **Framework**: FastAPI
- **Validation**: Pydantic
- **Database**: PostgreSQL (SQLAlchemy ORM)
- **AI**: Google Gemini API
- **Deployment**: Docker

## Setup

### Prerequisites

- Docker
- Gemini API Key
- PostgreSQL Database URL

### Running with Docker

1. Create a `.env` file with your credentials:

   ```env
   GEMINI_API_KEY=your_key_here
   DATABASE_URL=postgresql://user:password@host:port/dbname
   ```

2. Build and run:

   ```bash
   docker build -t resume-screener .
   docker run -p 8000:8000 --env-file .env resume-screener
   ```

3. Access API docs at `http://localhost:8000/docs`.

### Using the Frontend

1. Ensure the backend is running (locally or via Docker).
2. Open `frontend/index.html` in your web browser.
3. Enter a Job Description and Resume text.
4. Click "Analyze Resume".

## Git Workflow

We use the Feature Branch Workflow:

- `main`: Production ready.
- `develop`: Integration branch.
- `feature/*`: Feature branches.

## License

MIT
