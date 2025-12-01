from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    domain = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    duration = Column(Integer, default=0)  # seconds
    user_id = Column(Integer)
