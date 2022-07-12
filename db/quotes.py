import sqlalchemy

from .base import metadata


quotes = sqlalchemy.Table(
    "quotes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("num_code", sqlalchemy.String),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.Float),
    sqlalchemy.Column("date", sqlalchemy.Date),
    sqlalchemy.Column("nominal", sqlalchemy.Integer),
)