"""empty message

Revision ID: e6a6002a65d6
Revises: b7f413d35d7f
Create Date: 2022-05-10 00:52:12.893734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6a6002a65d6'
down_revision = 'b7f413d35d7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('post_user_id_fkey', 'post', type_='foreignkey')
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.create_foreign_key('post_user_id_fkey', 'post', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
