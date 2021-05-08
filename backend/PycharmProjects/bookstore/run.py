from fastapi import FastAPI, HTTPException, Depends
from routes.v1 import app_v1
from routes.v2 import app_v2
from starlette.requests import Request
from starlette.responses import Response
from datetime import datetime

from fastapi.security import OAuth2PasswordRequestForm
from utils.security import authenticate_user, create_jwt_token, check_jwt_token
from models.jwt_user import JWTUser
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI()
app.include_router(app_v1, prefix="/v1", dependencies=[Depends(check_jwt_token)])
app.include_router(app_v2, prefix="/v2", dependencies=[Depends(check_jwt_token)])


@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    jwt_user_dict = {"username": form_data.username,
                     "password": form_data.password}
    jwt_user = JWTUser(**jwt_user_dict)
    user = authenticate_user(jwt_user)
    if None is user:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    jwt_token = create_jwt_token(user)
    return {"access_token": jwt_token}


@app.middleware("http")
async def middleware(request: Request, call_next):
    start_time = datetime.utcnow()
    # example 1. modify request
    # if not str(request.url).__contains__("/token"):
    if not any(word in str(request.url) for word in ["/token", "/docs", "/openapi.json"]):
        try:
            jwt_token = request.headers["Authorization"].split("Bearer ")[1]
            is_valid = check_jwt_token(jwt_token)
        except Exception as e:
            is_valid = False
        if not is_valid:
            return Response("Unau thorized", status_code=HTTP_401_UNAUTHORIZED)

    response = await call_next(request)

    # example 2. modify response
    excution_time = (datetime.utcnow() - start_time).microseconds
    response.headers["x-excution-time"] = str(excution_time)
    return response

