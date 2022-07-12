from .quotes import quotes
from .base import engine, metadata


metadata.create_all(bind=engine)