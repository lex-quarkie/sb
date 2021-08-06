from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.types import Numeric
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class WeightCategory(Base):
    __tablename__ = "weight_category"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    min_weight = Column(Numeric(precision=5, scale=2), nullable=False)
    max_weight = Column(
        Numeric(precision=5, scale=2), nullable=False
    )  # kg # 63.8 70.2 75 81.8 88 88+

    fighters = relationship("Fighter", backref="weight_category")
