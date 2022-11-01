"""init

Revision ID: 4e2deabd9931
Revises: 
Create Date: 2022-11-01 16:40:04.060860

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4e2deabd9931'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('phone_number', sa.String(length=16), nullable=True),
    sa.Column('creation_date', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('child')
    op.drop_table('parent')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parent',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('datetime_tz', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('datetime_not_tz', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('creation_date_tz', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('creation_date_not_tz', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='parent_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('child',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('parent_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['parent.id'], name='child_parent_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='child_pkey')
    )
    op.drop_table('user')
    # ### end Alembic commands ###