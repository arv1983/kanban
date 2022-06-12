"""empty message

Revision ID: 544ccdc938bc
Revises: 2a53395ca0af
Create Date: 2022-06-12 09:34:04.702353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '544ccdc938bc'
down_revision = '2a53395ca0af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('GroupsModel_members_fkey', 'GroupsModel', type_='foreignkey')
    op.drop_column('GroupsModel', 'members')
    op.drop_constraint('MembersModel_id_member_fkey', 'MembersModel', type_='foreignkey')
    op.drop_column('MembersModel', 'id_group')
    op.drop_column('MembersModel', 'id_member')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('MembersModel', sa.Column('id_member', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('MembersModel', sa.Column('id_group', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('MembersModel_id_member_fkey', 'MembersModel', 'post', ['id_member'], ['id'])
    op.add_column('GroupsModel', sa.Column('members', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('GroupsModel_members_fkey', 'GroupsModel', 'MembersModel', ['members'], ['id'])
    # ### end Alembic commands ###
