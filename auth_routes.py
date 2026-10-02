from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from auth_db import connect_db, register_user
import hashlib

router = APIRouter()


class User(BaseModel):
    username: str
    password: str


@router.post("/register")
def register(user: User):
    if len(user.password) < 8:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters"
        )

    if register_user(user.username, user.password):
        return {"message": "Registration successful"}

    raise HTTPException(
        status_code=400,
        detail="Username already exists"
    )


@router.post("/login")
def login(user: User):
    hashed = hashlib.sha256(
        user.password.encode()
    ).hexdigest()

    conn = connect_db()
    result = conn.execute(
        "SELECT id FROM users WHERE username=? AND password=?",
        (user.username, hashed)
    ).fetchone()
    conn.close()

    if result:
        return {
            "message": "Login successful",
            "user_id": result[0]
        }

    raise HTTPException(
        status_code=401,
        detail="Invalid username or password"
    )
