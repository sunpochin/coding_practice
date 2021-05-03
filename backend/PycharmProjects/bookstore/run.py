from fastapi import FastAPI, Body, Header
from models.author import Author
from models.book import Book
from models.user import User

app = FastAPI()

@app.get("/hello")
async def hello_world():
    return {"Hello fastapi world!"}

@app.post("/user")
async def post_user(user: User, x_custom: str = Header("default header") ):
    return {"request USER:": user, "request custom header": x_custom}

@app.get("/user")
async def get_user_validation(password:str):
    return {"QUERY parameter ": password}

@app.get("/book/{isbn}", response_model=Book, response_model_include=["name"] )
async def get_book_with_isbn(isbn: str):
    author_dict = {
        "name": "author1",
        "book": ["book1", "book2"]
    }
    author1 = Author(**author_dict)
    book_dict = {
        "isbn": "isbn1",
        "name": "book1",
        "year": 2019,
        "author": author1
    }
    book1 = Book(**book_dict)
    return book1

# @app.get("/book/{isbn}")
# async def get_book_with_isbn(isbn: str):
#     return {"Query CHANGABLE parameter ": isbn}

@app.get("/author/{id}/book")
async def get_authors_books(id: int, category: str, order: str = "asc"):
    return {"Both pass and query parameter ": order + category + str(id) }

@app.patch("/author/name")
async def patch_author_name(name: str = Body(..., embed=True) ):
    return {"name in body": name}

@app.post("/user/author")
async def post_user_and_author(user: User, author: Author, bookstore_name: str = Body(..., embed=True) ):
    return {"user": user, "author": author, "bookstore_name": bookstore_name}
