"""create

Revision ID: 75b07e2ac19d
Revises: 
Create Date: 2019-11-07 20:19:29.002144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75b07e2ac19d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player', sa.String(length=50), nullable=True),
    sa.Column('gamedate', sa.Date(), nullable=True),
    sa.Column('gamenumber', sa.Integer(), nullable=True),
    sa.Column('dumberrors', sa.Integer(), nullable=True),
    sa.Column('firstorsecondover', sa.Integer(), nullable=True),
    sa.Column('kills', sa.Integer(), nullable=True),
    sa.Column('attackerrors', sa.Integer(), nullable=True),
    sa.Column('totalattacks', sa.Integer(), nullable=True),
    sa.Column('assists', sa.Integer(), nullable=True),
    sa.Column('settingerrors', sa.Integer(), nullable=True),
    sa.Column('aces', sa.Integer(), nullable=True),
    sa.Column('serveattempts', sa.Integer(), nullable=True),
    sa.Column('serveerrors', sa.Integer(), nullable=True),
    sa.Column('receiveattempts', sa.Integer(), nullable=True),
    sa.Column('receiveerrors', sa.Integer(), nullable=True),
    sa.Column('digs', sa.Integer(), nullable=True),
    sa.Column('digerrors', sa.Integer(), nullable=True),
    sa.Column('blocks', sa.Integer(), nullable=True),
    sa.Column('blockassists', sa.Integer(), nullable=True),
    sa.Column('blockerrors', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stats')
    # ### end Alembic commands ###
