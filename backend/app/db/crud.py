from sqlalchemy.orm import Session

from app.db.models import (
    Character,
    Town,
    State,
    Game
)


def get_char_by_id(
    db: Session,
    id: int,
):
    return db.query(Character).filter(Character.id == id).first()


def get_town_by_id(
    db: Session,
    id: int,
):
    return db.query(Town).filter(Town.id == id).first()


def get_state_by_id(
    db: Session,
    id: int,
):
    return db.query(State).filter(State.id == id).first()


def get_game_by_id(
    db: Session,
    id: int,
):
    return db.query(Game).filter(Game.id == id).first()
