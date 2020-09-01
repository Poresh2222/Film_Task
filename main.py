import uvicorn
from fastapi import FastAPI

from fastapi import Header
from typing import List

from Api.schemas import FilmIn, FilmOut, FilmUpdate
from Db.crud import FilmDbMan as crud
from Db.db import db


app = FastAPI()

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.get('/', response_model=List[FilmOut])
async def get_films():
    return await crud.get_all_films()

@app.get('/{id}/', response_model=FilmOut)
async def get_film(id: int):
    film = await crud.get_film(id)

    return film

@app.post('/', response_model=FilmOut, status_code=201)
async def add_film(payload: FilmIn):
    film = await crud.add_film(payload)
    responce = {
        'id': film,
        **payload.dict()
    }

    return responce

@app.put('/{id}/', response_model=FilmOut)
async def change_film(id: int, payload: FilmUpdate):
    film = await crud.get_film(id)
    update_data = payload.dict(exclude_unset=True)
    film_in_db = FilmIn(**film)
    updated_film = film_in_db.copy(update=update_data)

    return await crud.update_film(id, updated_film)

@app.delete('/{id}', response_model=None)
async def delete_film(id: int):
    return await crud.delete_film(id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)    