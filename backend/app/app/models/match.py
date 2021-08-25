from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from app import models
from app.db.base_class import Base


class Match(Base):
    __tablename__ = "match"
    id = Column(Integer, primary_key=True, index=True)
    first_fighter_id = Column(Integer, ForeignKey("fighter.id"), nullable=False)
    second_fighter_id = Column(Integer, ForeignKey("fighter.id"), nullable=False)

    first_fighter = relationship("Fighter", foreign_keys="[Match.first_fighter_id]")
    second_fighter = relationship("Fighter", foreign_keys="[Match.second_fighter_id]")
    match_odds = relationship("MatchEventOdds")
    # created_at = Column(DateTime, default=datetime.now)
    # updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    # start_time = Column(DateTime, nullable=True)