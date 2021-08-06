from typing import Optional

from pydantic import BaseModel


class FighterBase(BaseModel):
    first_name: str
    last_name: str
    photo_url: Optional[str]
    city: Optional[str]
    weight_category_id: int

    class Config:
        orm_mode = True

class FighterInDBBase(FighterBase):
    id: Optional[int] = None


