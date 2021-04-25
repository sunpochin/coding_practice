from fastapi import FastAPI
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
    return {"QUERY parameter: ":password}