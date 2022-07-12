from pydantic import BaseModel
from typing import Optional
from datetime import date 

class Quotes(BaseModel):
    id: Optional[int]
    num_code: str
    name: str
    price: float
    date: date
    nominal: int
    

class QuotesIn(BaseModel):
    num_code: str
    name: str
    price: float
    date: date
    nominal: int