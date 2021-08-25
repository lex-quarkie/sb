from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import Depends, FastAPI


def get_fighters(db: Session, skip: int, limit: int):
    return db.query(models.Fighter).offset(skip).limit(limit).all()


def get_fighter(db: Session, id: int):
    return db.query(models.Fighter).get(id)
