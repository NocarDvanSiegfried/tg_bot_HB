"""Add responsible field to birthdays table

Revision ID: 003_add_responsible_to_birthdays
Revises: 002_fix_user_id_bigint
Create Date: 2024-12-20 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003_add_responsible_to_birthdays'
down_revision = '002_fix_user_id_bigint'
branch_labels = None
depends_on = None


def upgrade():
    """Добавить поле responsible в таблицу birthdays."""
    op.add_column('birthdays', sa.Column('responsible', sa.String(255), nullable=True))


def downgrade():
    """Удалить поле responsible из таблицы birthdays."""
    op.drop_column('birthdays', 'responsible')

