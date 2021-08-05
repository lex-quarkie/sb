from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship


class MatchEvent(Base):
    __tablename__ = 'match_event'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)