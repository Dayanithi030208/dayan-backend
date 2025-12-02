from pydantic import BaseModel

class ActivityCreate(BaseModel):
    url: str
    domain: str
    duration: int
