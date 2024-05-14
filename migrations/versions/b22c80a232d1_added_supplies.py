"""added_supplies

Revision ID: b22c80a232d1
Revises: a5dea104446c
Create Date: 2024-05-14 21:36:37.575902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b22c80a232d1'
down_revision: Union[str, None] = 'a5dea104446c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('supplies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('drug_id', sa.Integer(), nullable=False),
    sa.Column('drug_amount', sa.Integer(), nullable=False),
    sa.Column('cost', sa.Integer(), nullable=False),
    sa.Column('assigned_datetime', sa.DateTime(), nullable=False),
    sa.Column('delivery_datetime', sa.DateTime(), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['drug_id'], ['drugs.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('supplies')
    # ### end Alembic commands ###