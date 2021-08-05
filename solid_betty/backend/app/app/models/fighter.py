from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Fighter(Base):
    __tablename__ = "fighter"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    photo_url = Column(String)
    city = Column(String)

    weight_category_id = Column(Integer, ForeignKey("weight_category.id"))
    league_id = Column(Integer, ForeignKey("league.id"))
