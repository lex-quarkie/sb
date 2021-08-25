from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class League(Base):
    __tablename__ = "league"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    min_rounds = Column(Integer, nullable=False)
    max_rounds = Column(Integer, nullable=False)
    fighters = relationship("Fighter", backref="league")
