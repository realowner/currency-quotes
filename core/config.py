from starlette.config import Config


config = Config('.env')
DATABASE_URL = config('DB_URL', cast=str, default='')
APP = config('APP', cast=str, default='')
DATE = config('DATE', cast=str, default='')