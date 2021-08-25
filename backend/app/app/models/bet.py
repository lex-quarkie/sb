from datetime import datetime

from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Bet(Base):
    __tablename__ = "bet"
    id = Column(Integer, primary_key=True, index=True)
    selected_event_id = Column(Integer, ForeignKey("match_event.id"))

    owner_id = Column(Integer, ForeignKey("user.id"))
    match_id = Column(Integer, ForeignKey("match.id"))

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
