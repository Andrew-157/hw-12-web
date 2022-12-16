"""unique link

Revision ID: 7d8b499d8ca5
Revises: 344d7a493da7
Create Date: 2022-12-16 09:38:58.588003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d8b499d8ca5'
down_revision = '344d7a493da7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('links', sa.Column(
        'link', sa.String(150), nullable=False, unique=True))


def downgrade() -> None:
    op.alter_column('links', sa.Column(
        'link', sa.String(150), nullable=False, unique=False))
