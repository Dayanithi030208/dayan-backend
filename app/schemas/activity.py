from pydantic import BaseModel
from datetime import datetime
from typing import Optional
class ActivityCreate(BaseModel):
    url: str
    domain: str
    duration: int

class ActivityResponse(BaseModel):
    id: int
    user_id: int
    url: str
    domain: Optional[str]=None
    duration: int
    timestamp: datetime

    model_config = {"from_attributes": True}  # for pydantic v2
