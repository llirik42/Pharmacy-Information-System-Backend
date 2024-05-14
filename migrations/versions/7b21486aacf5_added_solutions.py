"""added_solutions

Revision ID: 7b21486aacf5
Revises: 3c7e0e103aba
Create Date: 2024-05-14 20:58:10.250684

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b21486aacf5'
down_revision: Union[str, None] = '3c7e0e103aba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('solutions',
    sa.Column('drug_id', sa.Integer(), nullable=False),
    sa.Column('dosage', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['drug_id'], ['drugs.id'], ),
    sa.PrimaryKeyConstraint('drug_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('solutions')
    # ### end Alembic commands ###