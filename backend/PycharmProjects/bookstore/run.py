from fastapi import FastAPI
# from models.author import Author
# from models.book import Book
from models.user import User

app = FastAPI()

@app.get("/hello")
async def hello_world():
    return {"Hello fastapi world!"}

@app.post("/user")
async def post_user(user: User):
    return {"request USER:": user}

@app.get("/user")
async def get_user_validation(password:str):
    return {"QUERY parameter ": password}

@app.get("/book/{isbn}")
async def get_book_with_isbn(isbn: str):
    return {"Query CHANGABLE parameter ": isbn}


@app.get("/author/{id}/book")
async def get_authors_books(id: int, category: str, order: str = "asc"):
    return {"Both pass and query parameter ": order + category + str(id) }


