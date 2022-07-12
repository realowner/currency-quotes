from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

import requests
import json

from models.quotes import Quotes, QuotesIn
from repositories.quotes import QuotesRepository
from .depends import get_quotes_repository

router = APIRouter()

@router.get('/', response_model=List[Quotes])
async def read_quotes(quotes: QuotesRepository=Depends(get_quotes_repository),):
    return await quotes.get_all()

@router.get('/fromapi', response_model=List[Quotes])
async def insert_from_api(quotes: QuotesRepository=Depends(get_quotes_repository),):
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    quot = json.loads(response.text)
    delete_result = await quotes.delete_all_quotes()
    if delete_result:
        return await quotes.create_many(quot=quot)
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Data cant be updated!")

@router.post('/', response_model=Quotes)
async def create_quotes(quot: QuotesIn, quotes: QuotesRepository=Depends(get_quotes_repository),):
    return await quotes.create_quotes(quot=quot)

@router.post('/showselected', response_model=List[Quotes])
async def show_selected(quots: List, quotes: QuotesRepository=Depends(get_quotes_repository),):
    return await quotes.get_by_name(name_list=quots)

@router.put('/', response_model=Quotes)
async def update_quotes(id: int, quot: QuotesIn, quotes: QuotesRepository=Depends(get_quotes_repository),):
    quot_data = await quotes.get_by_id(id=id)
    if quot_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found!")
    return await quotes.update_quotes(id=id, quot=quot)

@router.delete('/')
async def delete_quotes(id: int, quotes: QuotesRepository=Depends(get_quotes_repository),):
    quot_data = await quotes.get_by_id(id=id)
    if quot_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found!")
    result = await quotes.delete_quotes(id=id)
    if result:
        return {"status": True}
    return {"status": False}