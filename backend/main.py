from fastapi import FastAPI

from app.database import Base, engine
from app.routes import insights as legacy_insights

from .api.routes import chat, health, memory

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Personal AI OS API")

app.include_router(health.router)
app.include_router(chat.router)
app.include_router(memory.router)
app.include_router(legacy_insights.router)


@app.get("/")
def root():
    return {"status": "ok"}
