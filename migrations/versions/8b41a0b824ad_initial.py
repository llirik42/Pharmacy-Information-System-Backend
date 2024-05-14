"""initial

Revision ID: 8b41a0b824ad
Revises: 0e1b9df7c58c
Create Date: 2024-05-14 17:13:17.402586

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b41a0b824ad'
down_revision: Union[str, None] = '0e1b9df7c58c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administration_routes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('administration_routes')
    # ### end Alembic commands ###
