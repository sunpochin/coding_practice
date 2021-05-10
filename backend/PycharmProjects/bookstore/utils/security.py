from passlib.context import CryptContext
from models.jwt_user import JWTUser
from datetime import datetime, timedelta
from utils.const import JWT_EXPIRATION_TIME_MINUTES, JWT_ALGORITHM, JWT_SECRET_KEY
import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import time
from utils.db_functions import db_check_token_user, db_check_jwt_username

oauth_schema = OAuth2PasswordBearer(tokenUrl="/token")

pwd_context = CryptContext(schemes=["bcrypt"])
# jwt_user_fake_db = [{}]
# jwt_user1 = {"username": "user1",
#              "password": "$2b$12$UrtAyvqalJ3TGHihAshD5uQBZynM4IitZofMuu81hXj2veoePFfai",
#              "disabled": False, "role": "admin"}
# fake_jwt_user1 = JWTUser(**jwt_user1)


def get_hashed_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        return False


# 1. Authenticate username and password to give JWT token
async def authenticate_user(user: JWTUser):
    potential_users = await db_check_token_user(user)
    is_valid = False
    for db_user in potential_users:
        if verify_password(user.password, db_user["password"]):
            is_valid = True
    if is_valid:
        user.role = "admin"
        return user
    # hashed_password = get_hashed_password(user.password)
    # user.password = hashed_password
    # is_valid = await db_check_token_user(user)
    # if is_valid:
    #     user.role = "admin"
    #     return user

    # if fake_jwt_user1.username == user.username:
    #     if verify_password(user.password, fake_jwt_user1.password):
    #         user.role = "admin"
    #         return user
    #         # return True
    # return None


# 2. Create access JWT token
async def create_jwt_token(user: JWTUser):
    expiration = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    jwt_payload = {"sub": user.username,
                   "role": user.role,
                   "exp": expiration}
    jwt_token = jwt.encode(jwt_payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return jwt_token


# 3. Check whether JWT token is correct
async def check_jwt_token(token: str = Depends(oauth_schema)):
    try:
        jwt_payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
        username = jwt_payload.get("sub")
        role = jwt_payload.get("role")
        expiration = jwt_payload.get("exp")
        # if datetime.utcnow() < expiration:
        if time.time() < expiration:
            is_valid = await db_check_jwt_username(username)
            if is_valid:
                return final_checks(role)

        # if time.time() < expiration:
        #     if fake_jwt_user1.username == username:
        #         return final_checks(username, role)
    except Exception as e:
        return False
        # raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    return False
    # raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    #     return HTTP_401_UNAUTHORIZED
    # return HTTP_401_UNAUTHORIZED


# 4. Last checking and returning the final result
def final_checks(role: str):
    if role == "admin":
        return True
    else:
        return False
    # raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    pass

# print(get_hashed_password("mysecret"))
# print(verify_password("mysecret", hashed) )
# print(get_hashed_password("pass1"))


print(get_hashed_password("secret"))
