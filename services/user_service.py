from fastapi import Depends
from repositories.user_repository import UserRepository
from schemas.user_schema import UserCreate

class UserService:
    def __init__(self, repository: UserRepository = Depends(UserRepository)):
        self.repository = repository

    async def create_user(self, user: UserCreate):
        return await self.repository.create_user(user)

    async def all_users(self):
        return await self.repository.all_users()