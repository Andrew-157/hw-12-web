"""drop data column

Revision ID: 344d7a493da7
Revises: 3c42c77cea4f
Create Date: 2022-12-15 11:29:36.250543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '344d7a493da7'
down_revision = '3c42c77cea4f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('links', 'agregated_data')


def downgrade() -> None:
    op.add_column('links', sa.Column('agregated_data', sa.String(200)))
