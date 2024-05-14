"""added_unique_constraints

Revision ID: f1a67bd3d0da
Revises: 693a9f89c3a1
Create Date: 2024-05-14 20:49:45.873861

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1a67bd3d0da'
down_revision: Union[str, None] = '693a9f89c3a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'customers', ['full_name', 'phone_number', 'address'])
    op.create_unique_constraint(None, 'prescriptions', ['diagnosis', 'patient_id', 'doctor_id', 'date'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'prescriptions', type_='unique')
    op.drop_constraint(None, 'customers', type_='unique')
    # ### end Alembic commands ###