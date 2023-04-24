from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.orm import Session

from app.db.session import get_db
import app.db.crud as crud
import app.db.schemas as schemas

router_rdr = APIRouter()


@router_rdr.get(
    '/chars/{char_id}',
    response_model=schemas.CharSchema
)
def read_char(
    char_id: int,
    db: Session = Depends(get_db)
):
    ans = crud.get_char_by_id(db, char_id)
    return ans


@router_rdr.get('/towns/{town_id}', response_model=schemas.TownSchema)
def read_town(town_id: int, db: Session = Depends(get_db)):
    ans = crud.get_town_by_id(db, town_id)
    return ans


@router_rdr.get('/states/{state_id}', response_model=schemas.StateSchema)
def read_state(state_id: int, db: Session = Depends(get_db)):
    ans = crud.get_state_by_id(db, state_id)
    return ans


@router_rdr.get('/game/{game_id}', response_model=schemas.GameSchema)
def read_game(game_id: int, db: Session = Depends(get_db)):
    print('yes')
    ans = crud.get_game_by_id(db, game_id)
    return ans
