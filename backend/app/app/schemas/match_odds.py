from pydantic import BaseModel


class MatchOddsBase(BaseModel):
    match_event_id: int
    match_id: int
    odds: int

    class Config:
        orm_mode = True
