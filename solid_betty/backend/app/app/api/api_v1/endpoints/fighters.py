from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.FighterBase])
def read_fighters(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100,
        current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Retrieve fighters
    """
    fighters = crud.crud_fighter.get_fighters(db=db, skip=skip, limit=limit)
    return fighters

@router.get("/<id>", response_model=schemas.FighterBase)
def read_fighter(
    id, db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve fighter
    """
    fighter = crud.crud_fighter.get_fighter(db=db, id=id)
    return fighter