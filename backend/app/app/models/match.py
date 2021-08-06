from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Match(Base):
    __tablename__ = "match"
    id = Column(Integer, primary_key=True, index=True)
    first_fighter_id = Column(Integer, ForeignKey("fighter.id"), nullable=False)
    second_fighter_id = Column(Integer, ForeignKey("fighter.id"), nullable=False)

    first_fighter = relationship("Fighter", foreign_keys="[Match.first_fighter_id]")
    second_fighter = relationship("Fighter", foreign_keys="[Match.second_fighter_id]")
