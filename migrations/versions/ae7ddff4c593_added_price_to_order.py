"""added price to order

Revision ID: ae7ddff4c593
Revises: 5633e542cc32
Create Date: 2021-12-06 14:17:02.595051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae7ddff4c593'
down_revision = '5633e542cc32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('price', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'price')
    # ### end Alembic commands ###
