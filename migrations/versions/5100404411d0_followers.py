"""followers

Revision ID: 5100404411d0
Revises: 63a029597c4d
Create Date: 2019-09-25 19:54:52.851489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5100404411d0'
down_revision = '63a029597c4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
