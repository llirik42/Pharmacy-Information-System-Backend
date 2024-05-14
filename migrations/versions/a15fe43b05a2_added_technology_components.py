"""added_technology_components

Revision ID: a15fe43b05a2
Revises: 599137aafa84
Create Date: 2024-05-14 22:03:21.830118

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a15fe43b05a2'
down_revision: Union[str, None] = '599137aafa84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('technology_components',
    sa.Column('technology_id', sa.Integer(), nullable=False),
    sa.Column('component_id', sa.Integer(), nullable=False),
    sa.Column('component_amount', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['component_id'], ['drugs.id'], ),
    sa.ForeignKeyConstraint(['technology_id'], ['technologies.id'], ),
    sa.PrimaryKeyConstraint('technology_id', 'component_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('technology_components')
    # ### end Alembic commands ###