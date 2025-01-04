from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user_models import User
from schemas.user_schema import UserCreate

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user: UserCreate):
        new_user = User(**user.model_dump())
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user

    async def all_users(self):
        result = await self.db.execute(select(User).where(User.is_active == True))
        return result.scalars().all()

    async def get_user(self, id: int):
        result = await self.db.execute(select(User).filter(User.id == id))
        return result.scalars().first()

    async def delete_user(self, id: int):
        result = await self.db.execute(select(User).filter(User.id == id))
        user = result.scalars().first()
        user.is_active = False
        await self.db.commit()
        await self.db.refresh(user)
        return user