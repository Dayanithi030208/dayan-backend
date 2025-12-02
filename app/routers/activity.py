from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.activity import ActivityCreate
from app.models.activity_model import Activity

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/track")
def track_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    log = Activity(
        user_id=1,  # TEMP: replace when JWT auth added
        url=activity.url,
        domain=activity.domain,
        duration=activity.duration,
    )
    db.add(log)
    db.commit()
    return {"status": "logged"}
