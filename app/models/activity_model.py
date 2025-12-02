from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    url = Column(String)
    domain = Column(String)
    duration = Column(Integer, default=0)  # time spent in seconds
    timestamp = Column(DateTime, default=datetime.utcnow)
