from pydantic import BaseModel


class Match(BaseModel):
    id: int
    first_fighter_id: int
    second_fighter_id: int