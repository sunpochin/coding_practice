from databases import Database

async def connect_db():
    db = Database("postgresql://admin:admin@localhost")