from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import SessionLocal


app = FastAPI(
    title="Darukaa.Earth API",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "ok",
            "database": "connected",
        }

    finally:
        db.close()
