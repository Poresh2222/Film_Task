from Db.models import Table1
from Api.schemas import FilmIn

from Db.db import db
import sqlalchemy


class FilmDbMan:
    @classmethod
    async def add_film(cls, payload: FilmIn):
        query = Table1.insert().values(**payload.dict())
        return await db.execute(query=query)

    @classmethod
    async def get_all_films(cls):
        query = Table1.select()
        return await db.fetch_all(query=query)

    @classmethod
    async def get_film(cla, id):
        query = Table1.select(Table1.c.id==id)
        return await db.fetch_one(query=query)

    @classmethod
    async def delete_film(cls, id: int):
        query = Table1.delete().where(Table1.c.id==id)
        return await db.execute(query=query)

    @classmethod
    async def update_film(cls, id: int, payload: FilmIn):
        query = (
            Table1
            .update()
            .where(Table1.c.id==id)
            .values(**payload.dict())
        )
        return await db.execute(query=query)