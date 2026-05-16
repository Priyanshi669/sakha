from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud
from ..analyzer import analyze_behavior

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/insights")
def get_insights(db: Session = Depends(get_db)):
    activities = crud.get_activities(db)
    result = analyze_behavior(activities)
    return result
