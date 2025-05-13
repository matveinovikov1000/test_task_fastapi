"""Initial migration

Revision ID: 3f8ff4ef3ff2
Revises: 
Create Date: 2025-05-13 21:52:52.475362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f8ff4ef3ff2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'urls',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('url', sa.String(), nullable=False),
        sa.Column('short_url', sa.String(10), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
