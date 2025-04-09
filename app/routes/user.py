from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.get("/login")
def login():
    return {"message": "Login route works"}

@router.post("/register")
def register(): 
    return {"message": "Register route works"}