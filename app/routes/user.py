from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.supabase import supabase

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

class UserRegister(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

@router.post("/register")
async def register(user: UserRegister):
    try:
        # Correct usage of sign_up method
        response = supabase.auth.sign_up({
            "email": user.email,
            "password": user.password
        })
        if response.get("user"):
            return {"message": "Registration successful", "data": response["user"]}
        else:
            raise HTTPException(status_code=400, detail="Registration failed. Please check your input.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login(user: UserLogin):
    try:
        # Correct usage of sign_in_with_password method
        response = supabase.auth.sign_in_with_password({
            "email": user.email,
            "password": user.password
        })
        if response.get("user"):
            return {"message": "Login successful", "data": response}
        else:
            raise HTTPException(status_code=400, detail="Invalid credentials")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid credentials")
