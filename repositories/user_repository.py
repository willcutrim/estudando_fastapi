from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user_models import User
from schemas.user_schema import UserCreate

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user: UserCreate):
        new_user = User(**user.dict())
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user

    async def all_users(self):
        result = await self.db.execute(select(User))
        return result.scalars().all()
