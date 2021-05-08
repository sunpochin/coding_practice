from fastapi import FastAPI, Body, Header, File, APIRouter
from models.user import User
from starlette.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from starlette.responses import Response

# app_v2 = FastAPI(openapi_prefix="/v2")
app_v2 = APIRouter()

@app_v2.post("/user", status_code=HTTP_201_CREATED)
async def post_user(user: User, x_custom: str = Header("default header") ):
    # return {"request body:": "it's version 2"}
    return {"request body": "it's version 2"}
