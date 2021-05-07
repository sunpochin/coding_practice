from fastapi import FastAPI, Body, Header, File, Depends, HTTPException
from models.author import Author
from models.book import Book
from models.user import User
from starlette.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from starlette.responses import Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from utils.security import authenticate_user, create_jwt_token, check_jwt_token
from models.jwt_user import JWTUser

app_v1 = FastAPI(openapi_prefix="/v1")
oauth_schema = OAuth2PasswordBearer(tokenUrl= "/token")

@app_v1.get("/hello")
async def hello_world():
    return {"Hello fastapi world!"}

@app_v1.post("/user", status_code=HTTP_201_CREATED)
async def post_user(user: User, x_custom: str = Header("default header"),
                    jwt: bool = Depends(check_jwt_token) ):
    return {"request USER:": user, "request custom header": x_custom}

@app_v1.get("/user")
async def get_user_validation(password:str):
    return {"QUERY parameter ": password}

@app_v1.get("/book/{isbn}", response_model=Book, response_model_include=["name"] )
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

# @app_v1.get("/book/{isbn}")
# async def get_book_with_isbn(isbn: str):
#     return {"Query CHANGABLE parameter ": isbn}

@app_v1.get("/author/{id}/book")
async def get_authors_books(id: int, category: str, order: str = "asc"):
    return {"Both pass and query parameter ": order + category + str(id) }

@app_v1.patch("/author/name")
async def patch_author_name(name: str = Body(..., embed=True) ):
    return {"name in body": name}

@app_v1.post("/user/author")
async def post_user_and_author(user: User, author: Author, bookstore_name: str = Body(..., embed=True) ):
    return {"user": user, "author": author, "bookstore_name": bookstore_name}

# multi-form request
@app_v1.post("/user/photo")
async def upload_user_photo(response: Response, profile_photo: bytes = File(...)):
    response.headers["x-file-size"] = str(len(profile_photo) )
    response.set_cookie(key="cookie-api", value="test")
    return {"file size": len(profile_photo) }

@app_v1.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends() ):
    jwt_user_dict = {"username": form_data.username,
                     "password": form_data.password}
    jwt_user = JWTUser(**jwt_user_dict)
    user = authenticate_user(jwt_user)
    if None is user:
        raise HTTPException(status_code= HTTP_401_UNAUTHORIZED)
    jwt_token = create_jwt_token(user)
    return {"token": jwt_token}

