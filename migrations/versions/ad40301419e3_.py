"""empty message

Revision ID: ad40301419e3
Revises: 0d542368ea29
Create Date: 2022-08-05 12:50:24.036685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad40301419e3'
down_revision = '0d542368ea29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shopping_list', sa.Column('ingredient', sa.String(), nullable=False))
    op.drop_column('shopping_list', 'item')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shopping_list', sa.Column('item', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('shopping_list', 'ingredient')
    # ### end Alembic commands ###
