from sqlalchemy import create_engine, MetaData
from databases import Database

from core.config import DATABASE_URL


database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(
    DATABASE_URL, 
    connect_args={
        "check_same_thread": False
    }
)