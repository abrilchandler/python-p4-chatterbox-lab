"""your message

Revision ID: dfb6e6151ca0
Revises: a457778ce1c3
Create Date: 2024-09-13 12:39:25.343458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfb6e6151ca0'
down_revision = 'a457778ce1c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('username', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'username')
    # ### end Alembic commands ###
