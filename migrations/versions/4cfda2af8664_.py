"""empty message

Revision ID: 4cfda2af8664
Revises: 9b77973248af
Create Date: 2021-02-19 05:23:32.738161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cfda2af8664'
down_revision = '9b77973248af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('player_draft_user',
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('draft_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['draft_id'], ['draft.id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('player_id', 'draft_id')
    )
    op.alter_column('draft', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('draft', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_table('player_draft_user')
    # ### end Alembic commands ###
