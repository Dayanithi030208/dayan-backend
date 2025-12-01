from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class Mood(Base):
    __tablename__ = "moods"

    id = Column(Integer, primary_key=True)
    mood = Column(String)
    note = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer)
