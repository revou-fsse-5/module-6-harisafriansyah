"""Migration

Revision ID: 1e3ac927627f
Revises: ba9550e1851a
Create Date: 2024-10-12 12:06:44.716397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e3ac927627f'
down_revision = 'ba9550e1851a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('species', sa.String(length=100), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('special_requirements', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('role', sa.String(length=50), nullable=True),
    sa.Column('schedule', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('feeding_schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('animal_id', sa.Integer(), nullable=False),
    sa.Column('enclosure_id', sa.Integer(), nullable=False),
    sa.Column('food_type', sa.String(length=100), nullable=False),
    sa.Column('feeding_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['animal_id'], ['animal.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feeding_schedule')
    op.drop_table('employee')
    op.drop_table('animal')
    # ### end Alembic commands ###
