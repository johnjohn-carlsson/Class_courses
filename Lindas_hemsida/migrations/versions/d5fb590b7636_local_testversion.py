"""Local testversion

Revision ID: d5fb590b7636
Revises: 495e285df5b5
Create Date: 2024-01-11 10:11:30.759348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5fb590b7636'
down_revision = '495e285df5b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tidningar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titel', sa.String(length=80), nullable=False),
    sa.Column('forfattare', sa.String(length=50), nullable=False),
    sa.Column('pris', sa.Float(), nullable=False),
    sa.Column('lagerantal', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tidningar')
    # ### end Alembic commands ###
