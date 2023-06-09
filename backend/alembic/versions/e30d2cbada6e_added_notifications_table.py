"""Added Notifications Table

Revision ID: e30d2cbada6e
Revises: 17f3b7e50a62
Create Date: 2022-11-30 20:04:46.542743

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e30d2cbada6e'
down_revision = '17f3b7e50a62'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(length=50), nullable=True),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notifications_id'), 'notifications', ['id'], unique=False)
    op.create_index(op.f('ix_notifications_message'), 'notifications', ['message'], unique=False)
    op.create_index(op.f('ix_notifications_title'), 'notifications', ['title'], unique=False)
    op.drop_table('light')
    op.drop_table('thermostat')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('thermostat',
    sa.Column('deviceid', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('humidity', mysql.FLOAT(), nullable=True),
    sa.Column('indoortemperature', mysql.FLOAT(), nullable=True),
    sa.Column('outdoortemperature', mysql.FLOAT(), nullable=True),
    sa.Column('date', mysql.DATETIME(), nullable=True),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('light',
    sa.Column('deviceid', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('brightness', mysql.FLOAT(), nullable=True),
    sa.Column('date', mysql.DATETIME(), nullable=True),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_index(op.f('ix_notifications_title'), table_name='notifications')
    op.drop_index(op.f('ix_notifications_message'), table_name='notifications')
    op.drop_index(op.f('ix_notifications_id'), table_name='notifications')
    op.drop_table('notifications')
    # ### end Alembic commands ###
