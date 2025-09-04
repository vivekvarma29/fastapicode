from fastapi import APIRouter, FastAPI

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "FAST API is working"}

