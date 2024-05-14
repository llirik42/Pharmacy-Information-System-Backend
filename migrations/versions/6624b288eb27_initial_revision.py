"""Initial revision

Revision ID: 6624b288eb27
Revises: bd8bf2a1a35b
Create Date: 2024-05-14 17:00:26.950202

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6624b288eb27'
down_revision: Union[str, None] = 'bd8bf2a1a35b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
