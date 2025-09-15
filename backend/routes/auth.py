from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from ..models.user import User
from ..config.db import get_db

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

users_db = {}

@router.post("/register")
def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User exists")
    users_db[user.username] = {
        "username": user.username,
        "password": pwd_context.hash(user.password)
    }
    return {"msg": "registered"}

@router.post("/login")
def login(user: User):
    db_user = users_db.get(user.username)
    if not db_user or not pwd_context.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": "fake-jwt-token"}