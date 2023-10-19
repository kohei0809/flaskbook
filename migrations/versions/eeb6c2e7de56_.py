"""empty message

Revision ID: eeb6c2e7de56
Revises: 48c053b6f059
Create Date: 2023-10-19 17:50:14.587579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eeb6c2e7de56'
down_revision = '48c053b6f059'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_image_tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_image_id', sa.String(), nullable=True),
    sa.Column('tag_name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_image_id'], ['user_images.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_image_tags')
    # ### end Alembic commands ###
