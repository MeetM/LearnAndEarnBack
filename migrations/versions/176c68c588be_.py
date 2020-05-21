"""empty message

Revision ID: 176c68c588be
Revises: 
Create Date: 2020-05-21 19:56:55.259932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '176c68c588be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nonceverify',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('eth_address', sa.String(length=1000), nullable=False),
    sa.Column('nonce', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('eth_address')
    )
    op.create_table('student',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('eth_address', sa.String(length=1000), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('student_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('eth_address')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('nonceverify')
    # ### end Alembic commands ###