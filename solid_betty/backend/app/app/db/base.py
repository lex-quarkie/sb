# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.match import Match # noqa
from app.models.user import User  # noqa
from app.models.weight_category import WeightCategory # noqa
