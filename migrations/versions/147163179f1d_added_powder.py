"""added_powder

Revision ID: 147163179f1d
Revises: 80e529d51d60
Create Date: 2024-05-14 20:35:11.726531

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '147163179f1d'
down_revision: Union[str, None] = '80e529d51d60'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('powders',
    sa.Column('drug_id', sa.Integer(), nullable=False),
    sa.Column('composite', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['drug_id'], ['drugs.id'], ),
    sa.PrimaryKeyConstraint('drug_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('powders')
    # ### end Alembic commands ###
