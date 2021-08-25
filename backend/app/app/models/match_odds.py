from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.types import Numeric
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class MatchEventOdds(Base):
    __tablename__ = "match_event_odds"
    id = Column(Integer, primary_key=True, index=True)
    match_event_id = Column(Integer, ForeignKey("match_event.id"), nullable=False)
    match_id = Column(Integer, ForeignKey("match.id"), nullable=False)
    odds = Column(Numeric(precision=4, scale=2), nullable=False)
