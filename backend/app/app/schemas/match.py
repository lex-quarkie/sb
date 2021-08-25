from typing import List, Optional
from pydantic import BaseModel

from app.schemas.fighter import FighterBase
from app.schemas.match_odds import MatchOddsBase


class MatchBase(BaseModel):
    first_fighter_id: Optional[int] = None
    second_fighter_id: Optional[int] = None

    class Config:
        orm_mode = True


class MatchInDB(MatchBase):
    id: Optional[int]

    class Config:
        orm_mode = True


class MatchResponse(MatchInDB):
    first_fighter: FighterBase
    second_fighter: FighterBase
    match_odds: Optional[List[MatchOddsBase]]

    class Config:
        orm_mode = True
