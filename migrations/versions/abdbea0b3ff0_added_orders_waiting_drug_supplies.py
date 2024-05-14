"""added_orders_waiting_drug_supplies

Revision ID: abdbea0b3ff0
Revises: 5e1198183d48
Create Date: 2024-05-14 21:54:54.114402

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abdbea0b3ff0'
down_revision: Union[str, None] = '5e1198183d48'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders_waiting_drug_supplies',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('drug_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['drug_id'], ['drugs.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['prescriptions.id'], ),
    sa.PrimaryKeyConstraint('order_id', 'drug_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders_waiting_drug_supplies')
    # ### end Alembic commands ###