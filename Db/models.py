from sqlalchemy import (Column, Integer, String, Table)
from Db.db import db, metadata, sqlalchemy


Table1 = Table(
    'FilmTable1',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('film', String),
    Column('comment', String),
    Column('stars', Integer),
)
