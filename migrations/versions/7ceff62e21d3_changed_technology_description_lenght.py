"""changed_technology_description_lenght

Revision ID: 7ceff62e21d3
Revises: 9c23d6f036fe
Create Date: 2024-05-14 21:44:17.985553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ceff62e21d3'
down_revision: Union[str, None] = '9c23d6f036fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('technologies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('drug_id', sa.Integer(), nullable=False),
    sa.Column('cooking_time', sa.Time(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=False),
    sa.ForeignKeyConstraint(['drug_id'], ['drugs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('technologies')
    # ### end Alembic commands ###
