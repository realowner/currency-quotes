from repositories.quotes import QuotesRepository
from db.base import database


def get_quotes_repository() -> QuotesRepository:
    return QuotesRepository(database)