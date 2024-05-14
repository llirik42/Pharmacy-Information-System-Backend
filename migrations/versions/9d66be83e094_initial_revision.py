"""Initial revision

Revision ID: 9d66be83e094
Revises: 6624b288eb27
Create Date: 2024-05-14 17:00:35.660824

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d66be83e094'
down_revision: Union[str, None] = '6624b288eb27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
