from pydantic import BaseModel
from typing import List, Optional


class FilmIn(BaseModel):
    film: str
    comment: str
    stars: int

    class Config:
        orm_mode = True


class FilmOut(FilmIn):
    id: int

    class Config:
        orm_mode = True


class FilmUpdate(FilmIn):
    film: Optional[str] = None
    comment: Optional[str] = None
    stars: Optional[int] = None

    class Config:
        orm_mode = True         