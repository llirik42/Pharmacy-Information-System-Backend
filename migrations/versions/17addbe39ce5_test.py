"""test

Revision ID: 17addbe39ce5
Revises: feb9c24954a3
Create Date: 2024-05-14 19:34:34.247694

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17addbe39ce5'
down_revision: Union[str, None] = 'feb9c24954a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'drugs', 'drug_types', ['critical_amount'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'drugs', type_='foreignkey')
    # ### end Alembic commands ###