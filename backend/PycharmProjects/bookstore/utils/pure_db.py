import asyncio
from utils.orm_db import authors
from databases import Database
from utils.const import *


async def connect_db():
    db = Database(DB_URL)
    await db.connect()
    return db


async def disconnect_db(db):
    await db.disconnect()


async def execute(query, is_many, values=None):
    db = await connect_db()
    if is_many:
        await db.execute_many(query=query, values=values)
    else:
        await db.execute(query=query, values=values)
    await disconnect_db(db)


async def fetch(query, is_one, values=None):
    db = await connect_db()

    if is_one:
        result = await db.fetch_one(query=query, values=values)
        if result is None:
            out = None
        else:
            out = dict(result)
    else:
        result = await db.fetch_all(query=query, values=values)
        if result is None:
            out = None
        else:
            out = []
            for row in result:
                out.append(dict(row))
    await disconnect_db(db)
    # print(out)
    return out


query_str = "insert into books values(:custom, :name, :author, :year)"

more_books = [{"custom": "isbn4", "name": "book4", "author": "author4", "year": 2004},
              {"custom": "isbn5", "name": "book5", "author": "author5", "year": 2005}]
single_book = {"isbn": "isbn1", "name": "book1", "author": "author1", "year": 2019}

# loop = asyncio.get_event_loop()
# loop.run_until_complete(execute(query_str, True, more_books))

# fetch one
fetch_str = "select * from books where isbn=:isbn"
fetch_result = {"isbn": "isbn4"}

# loop = asyncio.get_event_loop()
# loop.run_until_complete(fetch(fetch_str, True, fetch_result))
#
# fetch_str = "select * from books"
# loop = asyncio.get_event_loop()
# loop.run_until_complete(fetch(fetch_str, False))


async def test_orm():
    query = authors.insert().values(id=1, name="author1", books=["book1", "book2"])
    await execute(query, False)
    query = authors.insert().values(id=2, name="author2", books=["book3", "book4"])
    await execute(query, False)

    query = authors.select().where(authors.c.id == 2)
    # query = authors.select()
    out = await fetch(query, True)
    print(out)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(test_orm())
