from typing import Optional

from pydantic import BaseModel


class FighterBase(BaseModel):
    first_name: str
    last_name: str
    weight_category_id: int


class FighterInDBBase(FighterBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True
