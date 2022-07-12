from .base import BaseRepository
from db.quotes import quotes
from models.quotes import Quotes, QuotesIn

from typing import Dict, List, Optional
from datetime import datetime


class QuotesRepository(BaseRepository):
    
    # Достаем все
    async def get_all(self) -> List[Quotes]:
        query = quotes.select()
        return await self.database.fetch_all(query)
    
    # Достаем по id
    async def get_by_id(self, id: int) -> Optional[Quotes]:
        query = quotes.select().where(quotes.c.id==id)
        secret_data = await self.database.fetch_one(query)
        if secret_data is None:
            return None
        return Quotes.parse_obj(secret_data)
    
    # Достаем по именам
    async def get_by_name(self, name_list: List) -> List[Quotes]:
        query = quotes.select().filter(quotes.c.name.in_(name_list))
        return await self.database.fetch_all(query)
    
    # Создаем данные
    async def create_quotes(self, quot: QuotesIn) -> Quotes:
        quotes_data = Quotes(
            num_code = quot.num_code,
            name = quot.name,
            price = quot.price,
            date = quot.date,
            nominal = quot.nominal
        )
        values = {**quotes_data.dict()}
        values.pop("id", None)
        query = quotes.insert().values(**values)
        quotes.id = await self.database.execute(query=query)
        return quotes_data
    
    # Обновляем данные
    async def update_quotes(self, id: int, quot: QuotesIn) -> Quotes:
        quotes_data = Quotes(
            id=id,
            num_code = quot.num_code,
            name = quot.name,
            price = quot.price,
            date = quot.date,
            nominal = quot.nominal
        )
        values = {**quotes_data.dict()}
        values.pop("id", None)
        query = quotes.update().where(quotes.c.id==id).values(**values)
        await self.database.execute(query=query)
        return quotes_data
    
    # Удаляем данные
    async def delete_quotes(self, id: int) -> bool:
        try:
            query = quotes.delete().where(quotes.c.id==id)
            await self.database.execute(query=query)
            return True
        except:
            return False
        
    # Удаляем все данные
    async def delete_all_quotes(self) -> bool:
        try:
            query = quotes.delete()
            await self.database.execute(query=query)
            return True
        except:
            return False
    
    # Добавление нескольких строк
    async def create_many(self, quot: Dict) -> List[Quotes]:
        quot_date = quot['Date'].split('T')[0]
        items = await self.create_list(quot['Valute'], quot_date)
        
        await self.database.execute_many(quotes.insert(), items)
        query = quotes.select()
        return await self.database.fetch_all(query)


    # Вспомогательный метод для формирования данных для запроса
    async def create_list(self, valutes, quot_date) -> List:
        item_list = []
        for valute in valutes:
            item_list.append({
                'num_code': valutes[valute]['NumCode'],
                'name': valutes[valute]['Name'],
                'price': valutes[valute]['Value'], 
                'date': datetime.strptime(quot_date, "%Y-%m-%d"),
                'nominal': valutes[valute]['Nominal']
            })
        return item_list
    
