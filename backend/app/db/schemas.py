from typing import List, Union

from pydantic import BaseModel, EmailStr


class MailModel(BaseModel):
    email: EmailStr


class TunedModel(BaseModel):
    class Config:
        orm_mode = True


class CharBase(TunedModel):
    id: int
    name: str
    dead: Union[bool, None]
    bio: str
    town_id: Union[int, None]


class TownBase(TunedModel):
    id: int
    name: str
    state_id: Union[int, None]


class StateBase(TunedModel):
    id: int
    name: str


class GameBase(TunedModel):
    id: int
    title: str
    about: str


class GameSchema(GameBase):
    chars: List[CharBase]
    states: List[StateBase]


class StateSchema(StateBase):
    towns_list: Union[List[TownBase], None]
    games: List[GameBase]


class TownSchema(TownBase):
    borned_list: Union[List[CharBase], None]


class CharSchema(CharBase):
    games: List[GameBase]
