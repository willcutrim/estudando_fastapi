from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from services.user_service import UserService
from config.database import get_db
from schemas.user_schema import UserCreate, UserResponse

router = APIRouter()

@router.post("/create_user", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)) -> UserResponse:
    user_service = UserService(db)
    return await user_service.create_user(user)

@router.get("/users", response_model=list[UserResponse], status_code=200)
async def get_users(db: AsyncSession = Depends(get_db)) -> list[UserResponse]:
    user_service = UserService(db)
    return await user_service.all_users()

@router.get("/{id}", response_model=UserResponse)
async def get_user(id: int, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    return await user_service.get_user(id)