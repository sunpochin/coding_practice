from fastapi.testclient import TestClient
from starlette.testclient import TestClient
from run import app
from utils.pure_db import *
import asyncio

client = TestClient(app)
loop = asyncio.get_event_loop()
from utils.security import *

def insert_user(username, password):
    query = """insert into users(username,password) values(:username, :password)"""
    hashed_password = get_hashed_password(password)
    values = {"username": username, "password": hashed_password}

    loop.run_until_complete(execute(query, False, values))


# def test_read_main():
#     print("client: ", client)
#     response = client.get("/")
#
#     print(response.json())
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}

def clear_db():
    query1 = """delete from users;"""
    query2 = """delete from authors;"""
    query3 = """delete from book;"""
    query4 = """delete from personel;"""

    loop.run_until_complete(execute(query1, False))
    loop.run_until_complete(execute(query2, False))
    loop.run_until_complete(execute(query3, False))
    loop.run_until_complete(execute(query4, False))


def test_token_successful():
    insert_user("user1", "pass1")
    response = client.post("/token", dict(username="user1", password="pass1"))

    print(response.json())
    assert response.status_code == 200
    assert "access_token" in response.json()

    clear_db()