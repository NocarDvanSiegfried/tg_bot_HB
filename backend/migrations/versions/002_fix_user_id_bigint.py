"""Исправить тип user_id на BigInteger для поддержки больших Telegram ID.

Revision ID: 002_fix_user_id_bigint
Revises: 001_initial
Create Date: 2025-12-09 00:30:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_fix_user_id_bigint'
down_revision = '001_initial'
branch_labels = None
depends_on = None


def upgrade():
    """Изменить тип user_id с INTEGER на BIGINT."""
    op.alter_column(
        'panel_access',
        'user_id',
        existing_type=sa.Integer(),
        type_=sa.BigInteger(),
        existing_nullable=False,
    )


def downgrade():
    """Откатить изменение типа user_id обратно на INTEGER."""
    # ВНИМАНИЕ: Это может привести к потере данных, если есть user_id > 2,147,483,647
    op.alter_column(
        'panel_access',
        'user_id',
        existing_type=sa.BigInteger(),
        type_=sa.Integer(),
        existing_nullable=False,
    )

