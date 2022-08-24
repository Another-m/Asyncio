

database = 'postgresql'
driver = '+asyncpg'
owner = 'netology_bd'
password = 'password'
host = 'localhost'
port = 5432
name = 'asyncio'
db_set_asyncio = f'{database}{driver}://{owner}:{password}@{host}:{port}/{name}'
db_set = f'{database}://{owner}:{password}@{host}:{port}/{name}'
