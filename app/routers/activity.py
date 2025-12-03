from fastapi import APIRouter, Depends,Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.activity import ActivityCreate
from app.models.activity_model import Activity
from app.schemas.activity import ActivityResponse
from app.utils.token import verify_token_and_get_user
from fastapi import HTTPException
from fastapi import APIRouter, Depends, Request


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.get("/list", response_model=list[ActivityResponse])
def list_activity(
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
    user_id: int = Depends(verify_token_and_get_user),
    db: Session = Depends(get_db),
):
    # newest first
    rows = (
        db.query(Activity)
        .filter(Activity.user_id == user_id)
        .order_by(Activity.timestamp.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
    return rows

@router.post("/track")
async def track_activity(
    request: Request,
    user_id: int = Depends(verify_token_and_get_user),
    db: Session = Depends(get_db)
):
    try:
        body = await request.json()
    except Exception as e:
        return {"error": "invalid json", "detail": str(e)}

    print("== Received /track body:", body, "USER:", user_id)

    # Validate data
    if not all(k in body for k in ("url", "domain", "duration")):
        return {"error": "missing fields", "received": list(body.keys())}

    url = body["url"]
    domain = body["domain"]
    duration = int(body["duration"])

    # Save in DB with correct user_id
    log = Activity(
        user_id=user_id,
        url=url,
        domain=domain,
        duration=duration
    )
    db.add(log)
    db.commit()

    return {"status": "logged"}
