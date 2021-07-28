from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class WeightCategory(Base):
    __tablename__ = "weight_category"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    max_weight = Column(Integer)  # kg # 63.8 70.2 75 81.8 88 88+

    fighters = relationship("Fighter", backref="weight_category")

