from fastapi import FastAPI, Body, Header, File, Request
from routes.v1 import app_v1
from routes.v2 import app_v2
from utils.security import check_jwt_token
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED
from datetime import datetime

app = FastAPI()
app.mount("/v1", app_v1)
app.mount("/v2", app_v2)

@app.middleware("http")
async def middleware(request: Request, call_next):
    start_time = datetime.utcnow()
    # example 1. modify request
    # if not str(request.url).__contains__("/token"):
    if not any(word in str(request.url) for word in ["/token", "/docs", "/openapi.json"]):
        try:
            jwt_token = request.headers["Authori"].split("Bearer ")[1]
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

