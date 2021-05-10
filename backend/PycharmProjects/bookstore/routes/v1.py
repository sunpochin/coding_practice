from fastapi import Body, Header, File, APIRouter
from models.author import Author
from models.book import Book
from models.user import User
from starlette.status import HTTP_201_CREATED
from starlette.responses import Response
from utils.security import check_jwt_token
from utils.db_functions import (db_insert_personel, db_check_personel,
                                db_get_book_with_isbn, db_get_author, db_check_fake)
# app_v1 = FastAPI(openapi_prefix="/v1")
app_v1 = APIRouter()


# async def post_user(user: User, x_custom: str = Header("default header"),
#                     # jwt: bool = Depends(check_jwt_token)
#                     ):
@app_v1.post("/user", status_code=HTTP_201_CREATED, tags=["User"])
async def post_user(user: User):
    await db_insert_personel(user)
    return {"result": "personel created"}
    # return {"request USER:": user, "request custom header": x_custom}


@app_v1.post("/login", tags=["User"])
async def get_user_validation(username: str = Body(...), password: str = Body(...)):
    result = await db_check_personel(username, password)
    return {"is_valid": result}
    # return {"QUERY parameter ": password}


@app_v1.get("/book/{isbn}", response_model=Book,
            response_model_include=["name", "year"], tags=["Book"])
async def get_book_with_isbn(isbn: str):
    book = await db_get_book_with_isbn(isbn)
    author = await db_get_author(book["author"])
    author_obj = Author(**author)
    book["author"] = author_obj
    book_result = Book(**book)
    return book_result

    # author_dict = {
    #     "name": "author1",
    #     "books": ["book1", "book2"]
    # }
    # author1 = Author(**author_dict)
    # book_dict = {
    #     "isbn": "isbn1",
    #     "name": "book1",
    #     "year": 2019,
    #     "author": author1
    # }
    # book1 = Book(**book_dict)
    # return book1

# @app_v1.get("/book/{isbn}")
# async def get_book_with_isbn(isbn: str):
#     return {"Query CHANGABLE parameter ": isbn}


@app_v1.get("/author/{id}/book", tags=["Book"])
async def get_authors_books(id: int, category: str, order: str = "asc"):
    return {"Both pass and query parameter ": order + category + str(id)}


@app_v1.patch("/author/name")
async def patch_author_name(name: str = Body(..., embed=True)):
    return {"name in body": name}


@app_v1.post("/user/author")
async def post_user_and_author(user: User, author: Author, bookstore_name: str = Body(..., embed=True)):
    return {"user": user, "author": author, "bookstore_name": bookstore_name}


# multi-form request
@app_v1.post("/user/photo")
async def upload_user_photo(response: Response, profile_photo: bytes = File(...)):
    response.headers["x-file-size"] = str(len(profile_photo))
    response.set_cookie(key="cookie-api", value="test")
    return {"file size": len(profile_photo)}
