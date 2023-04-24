"""empty message

Revision ID: 6f2013d1b65e
Revises: bbab56fecc7a
Create Date: 2023-04-20 03:54:22.127165+03:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f2013d1b65e'
down_revision = 'bbab56fecc7a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    from app.db.models import (
        games_and_chars_table,
        games_and_states_table,
        Game,
        State,
        Town,
        Character
    )

    op.bulk_insert(
        Game.__table__,
        [
            {
                'id': 1,
                'title': 'Red dead Redemption',
                'about': (
                    'Red Dead Redemption is a 2010 action-adventure game '
                    'developed by Rockstar San Diego and published '
                    'by Rockstar Games.'
                )
            },
            {
                'id': 2,
                'title': 'Red Dead Redemption II',
                'about': (
                    'Red Dead Redemption 2 is a 2018 action-adventure game '
                    'developed and published by Rockstar Games. The game is '
                    'the third entry in the Red Dead series and a prequel to '
                    'the 2010 game Red Dead Redemption.'
                )
            }
        ]
    )

    op.bulk_insert(
        State.__table__,
        [
            {
                'id': 1,
                'name': 'West Elizabeth'
            },
            {
                'id': 2,
                'name': 'Lemoyne'
            },
            {
                'id': 3,
                'name': 'New Austin'
            }
        ]
    )

    op.bulk_insert(
        Town.__table__,
        [
            {
                'id': 1,
                'name': 'Saint Denis',
                'state_id': 2
            },
            {
                'id': 2,
                'name': 'Blackwater',
                'state_id': 1
            },
            {
                'id': 3,
                'name': 'Armadillo',
                'state_id': 3
            },
            {
                'id': 4,
                'name': 'Valentine',
                'state_id': None
            }
        ]
    )

    op.bulk_insert(
        Character.__table__,
        [
            {
                'id': 1,
                'name': 'Arthur Morgan',
                'dead': True,
                'bio': (
                    'Arthur Morgan is a cold, brooding outlaw who often resorts'
                    ' to violence and has very few qualms about killing. At his '
                    'worst Arthur could be extremely ruthless and completely '
                    'unsympathetic to the people he hurts.'
                )
            },
            {
                'id': 2,
                'name': 'John Marston',
                'dead': True,
                'bio': (
                    'John Marston is a recurring character in the Red Dead '
                    'series, appearing as a central character and the primary'
                    ' protagonist of Red Dead Redemption, and as a central '
                    'character and the secondary protagonist of Red Dead '
                    'Redemption 2.'
                )
            },
            {
                'id': 3,
                'name': 'Jack Marston',
                'dead': False,
                'bio': (
                    'John "Jack" Marston Jr. is a recurring character in the Red'
                    ' Dead series, appearing as a central character and the '
                    'secondary protagonist of Red Dead Redemption, and as a '
                    'supporting character in Red Dead Redemption 2.'
                )
            }
        ]
    )

    op.bulk_insert(
        games_and_chars_table,
        [
            {
                'game_id': 1,
                'character_id': 2
            },
            {
                'game_id': 1,
                'character_id': 3
            },
            {
                'game_id': 2,
                'character_id': 1
            },
            {
                'game_id': 2,
                'character_id': 2
            },
            {
                'game_id': 2,
                'character_id': 3
            },
        ]
    )

    op.bulk_insert(
        games_and_states_table,
        [
            {
                'game_id': 1,
                'state_id': 1
            },
            {
                'game_id': 1,
                'state_id': 3
            },
            {
                'game_id': 2,
                'state_id': 1
            },
            {
                'game_id': 2,
                'state_id': 2
            },
            {
                'game_id': 2,
                'state_id': 3
            }
        ]
    )


def downgrade() -> None:
    pass
