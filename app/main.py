from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router
from app.core.config import settings
from app.db.session import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to AI-Powered Resume Screener API"}
