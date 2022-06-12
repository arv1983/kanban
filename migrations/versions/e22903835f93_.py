"""empty message

Revision ID: e22903835f93
Revises: 326b72b1f510
Create Date: 2022-06-12 15:40:46.793831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e22903835f93'
down_revision = '326b72b1f510'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(), nullable=True),
    sa.Column('email', sa.Unicode(), nullable=True),
    sa.Column('password', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin', sa.Integer(), nullable=True),
    sa.Column('name', sa.Unicode(), nullable=True),
    sa.ForeignKeyConstraint(['admin'], ['tb_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.Column('groups_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['groups_id'], ['tb_groups.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['tb_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Unicode(), nullable=True),
    sa.Column('description', sa.Unicode(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['tb_groups.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tb_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_post')
    op.drop_table('tb_members')
    op.drop_table('tb_groups')
    op.drop_table('tb_users')
    # ### end Alembic commands ###