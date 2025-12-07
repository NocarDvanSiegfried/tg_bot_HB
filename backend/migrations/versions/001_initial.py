"""Initial migration

Revision ID: 001_initial
Revises: 
Create Date: 2024-12-08

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '001_initial'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'birthdays',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('full_name', sa.String(length=255), nullable=False),
        sa.Column('company', sa.String(length=255), nullable=False),
        sa.Column('position', sa.String(length=255), nullable=False),
        sa.Column('birth_date', sa.Date(), nullable=False),
        sa.Column('comment', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_birthdays_id'), 'birthdays', ['id'], unique=False)
    op.create_index(op.f('ix_birthdays_full_name'), 'birthdays', ['full_name'], unique=False)
    op.create_index(op.f('ix_birthdays_company'), 'birthdays', ['company'], unique=False)
    op.create_index(op.f('ix_birthdays_position'), 'birthdays', ['position'], unique=False)
    op.create_index(op.f('ix_birthdays_birth_date'), 'birthdays', ['birth_date'], unique=False)
    op.create_index('idx_birthday_search', 'birthdays', ['full_name', 'company', 'position'], unique=False)

    op.create_table(
        'responsible_persons',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('full_name', sa.String(length=255), nullable=False),
        sa.Column('company', sa.String(length=255), nullable=False),
        sa.Column('position', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_responsible_persons_id'), 'responsible_persons', ['id'], unique=False)
    op.create_index(op.f('ix_responsible_persons_full_name'), 'responsible_persons', ['full_name'], unique=False)
    op.create_index(op.f('ix_responsible_persons_company'), 'responsible_persons', ['company'], unique=False)
    op.create_index(op.f('ix_responsible_persons_position'), 'responsible_persons', ['position'], unique=False)
    op.create_index('idx_responsible_search', 'responsible_persons', ['full_name', 'company', 'position'], unique=False)

    op.create_table(
        'date_responsible_assignments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('responsible_person_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['responsible_person_id'], ['responsible_persons.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('date', 'responsible_person_id', name='idx_date_responsible_unique')
    )
    op.create_index(op.f('ix_date_responsible_assignments_id'), 'date_responsible_assignments', ['id'], unique=False)
    op.create_index(op.f('ix_date_responsible_assignments_date'), 'date_responsible_assignments', ['date'], unique=False)

    op.create_table(
        'professional_holidays',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_professional_holidays_id'), 'professional_holidays', ['id'], unique=False)
    op.create_index(op.f('ix_professional_holidays_date'), 'professional_holidays', ['date'], unique=False)

    op.create_table(
        'panel_access',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('accessed_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_panel_access_id'), 'panel_access', ['id'], unique=False)
    op.create_index(op.f('ix_panel_access_user_id'), 'panel_access', ['user_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_panel_access_user_id'), table_name='panel_access')
    op.drop_index(op.f('ix_panel_access_id'), table_name='panel_access')
    op.drop_table('panel_access')
    op.drop_index(op.f('ix_professional_holidays_date'), table_name='professional_holidays')
    op.drop_index(op.f('ix_professional_holidays_id'), table_name='professional_holidays')
    op.drop_table('professional_holidays')
    op.drop_index(op.f('ix_date_responsible_assignments_date'), table_name='date_responsible_assignments')
    op.drop_index(op.f('ix_date_responsible_assignments_id'), table_name='date_responsible_assignments')
    op.drop_table('date_responsible_assignments')
    op.drop_index('idx_responsible_search', table_name='responsible_persons')
    op.drop_index(op.f('ix_responsible_persons_position'), table_name='responsible_persons')
    op.drop_index(op.f('ix_responsible_persons_company'), table_name='responsible_persons')
    op.drop_index(op.f('ix_responsible_persons_full_name'), table_name='responsible_persons')
    op.drop_index(op.f('ix_responsible_persons_id'), table_name='responsible_persons')
    op.drop_table('responsible_persons')
    op.drop_index('idx_birthday_search', table_name='birthdays')
    op.drop_index(op.f('ix_birthdays_birth_date'), table_name='birthdays')
    op.drop_index(op.f('ix_birthdays_position'), table_name='birthdays')
    op.drop_index(op.f('ix_birthdays_company'), table_name='birthdays')
    op.drop_index(op.f('ix_birthdays_full_name'), table_name='birthdays')
    op.drop_index(op.f('ix_birthdays_id'), table_name='birthdays')
    op.drop_table('birthdays')

