from fastapi import FastAPI

from app.database import Base as LegacyBase, engine as legacy_engine
from app.routes import insights as legacy_insights

from .api.routes import chat, health, memory
from .db.sqlite import Base as CoreBase, engine as core_engine
from .models import db_models

LegacyBase.metadata.create_all(bind=legacy_engine)
CoreBase.metadata.create_all(bind=core_engine)

app = FastAPI(title="Personal AI OS API")

app.include_router(health.router)
app.include_router(chat.router)
app.include_router(memory.router)
app.include_router(legacy_insights.router)


@app.get("/")
def root():
    return {"status": "ok"}
