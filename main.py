from fastapi import FastAPI
import uvicorn

from db.base import database
from endpoints import quotes


def create_application(title):
    application = FastAPI(title=title)
    return application

app = create_application(title="Currency Quotes")
app.include_router(quotes.router, prefix="/quotes", tags=["quotes"])

@app.on_event('startup')
async def startup():
    await database.connect()
    
@app.get('/')
def index():
    return 'index'

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)