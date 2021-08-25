from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.MatchResponse])
def read_matches(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve matches
    """
    matches = crud.crud_match.get_matches(db=db, skip=skip, limit=limit)
    return matches


@router.get("/<id>", response_model=schemas.MatchResponse)
def read_match(
    id,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve matches
    """
    match = crud.crud_match.get_match(db=db, id=id)
    return match


@router.post("/", response_model=schemas.MatchResponse)
def create_match(db: Session = Depends(deps.get_db), *, obj_in: schemas.MatchBase,
                 current_user: models.User = Depends(deps.get_current_active_superuser)):
    match = crud.crud_match.create_match(db=db, obj_in=obj_in)
    return match


@router.get("/redis_test")
def test_redis():
    return {"status": "Ok"}
