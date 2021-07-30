"""empty message

Revision ID: f1daccf5e021
Revises: 56ba6e293af7
Create Date: 2021-07-30 10:57:39.848014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1daccf5e021'
down_revision = '56ba6e293af7'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""insert into weight_category values 
               (1,'До 63.8 кг', 45.0, 63.8), 
               (2,'До 70.2 кг', 63.81, 70.2),
               (3,'До 81.8 кг', 70.21, 81.8),
               (4,'До 88 кг', 81.81, 88),
               (5,'Свыше 88', 88.1, 180);
               """)


def downgrade():
    op.execute("""delete from weight_category;""")
