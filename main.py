from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn

from core.config import APP, DATE

from db.base import database
from endpoints import quotes


def create_application(title):
    application = FastAPI(title=title)
    return application

app = create_application(title="Currency Quotes")
app.include_router(quotes.router, prefix="/quotes", tags=["quotes"])
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],) 

@app.on_event('startup')
async def startup():
    await database.connect()
    
@app.get('/')
def index():
    return {
        'app': APP,
        'tool': 'FastApi',
        'available endpionts': '/docs/',
        'developers': {
            'EvSE': {
                'github': 'https://github.com/realowner'
            }
        },
        'date': DATE
    }

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)