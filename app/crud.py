from sqlalchemy.orm import Session
from . import models


def get_activities(db: Session):
    return db.query(models.Activity).all()


def create_activity(db: Session, activity):
    db_activity = models.Activity(type=activity.type, duration=activity.duration)
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity
