"""empty message

Revision ID: 2fd14bc1ed64
Revises: 80d951552b35
Create Date: 2023-04-20 01:52:10.209883+03:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fd14bc1ed64'
down_revision = '80d951552b35'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('about', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('states',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('games_and_states_table',
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.ForeignKeyConstraint(['state_id'], ['states.id'], ),
    sa.PrimaryKeyConstraint('game_id', 'state_id')
    )
    op.create_table('towns',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['state_id'], ['states.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('dead', sa.Boolean(), nullable=True),
    sa.Column('bio', sa.String(), nullable=False),
    sa.Column('town_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['town_id'], ['towns.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('games_and_chars_table',
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.PrimaryKeyConstraint('game_id', 'character_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games_and_chars_table')
    op.drop_table('characters')
    op.drop_table('towns')
    op.drop_table('games_and_states_table')
    op.drop_table('states')
    op.drop_table('games')
    # ### end Alembic commands ###
