from pydantic import BaseModel


class ActivityCreate(BaseModel):
    type: str
    duration: float
