from fastapi import APIRouter, Depends
from services.user_service import UserService
from schemas.user_schema import UserCreate, UserResponse

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, service: UserService = Depends()):
    return await service.create_user(user)

@router.get("/users", response_model=UserResponse)
async def all_users(id: int, service: UserService = Depends()):
    return await service.get_user(id)