from sqlalchemy import Column, Integer, String, Float
from .database import Base


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)  # learning, coding, etc.
    duration = Column(Float)  # in hours
