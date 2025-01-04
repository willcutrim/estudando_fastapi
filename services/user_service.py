from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.user_repository import UserRepository
from schemas.user_schema import UserCreate
from config.database import get_db

class UserService:
    def __init__(self, db: AsyncSession = Depends(get_db)):
        self.repository = UserRepository(db)

    async def create_user(self, user: UserCreate):
        return await self.repository.create_user(user)

    async def all_users(self):
        return await self.repository.all_users()