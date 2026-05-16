from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from ..db.sqlite import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True)
    user_message = Column(String)
    assistant_response = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)


class Memory(Base):
    __tablename__ = "memories"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    memory_type = Column(String, index=True)
    importance_score = Column(Float, default=1.0)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    chroma_id = Column(String, index=True)
