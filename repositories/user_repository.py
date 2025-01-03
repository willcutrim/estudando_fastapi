from models.user_models import User
from sqlalchemy.ext.asyncio import AsyncSession

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user):
        new_user = User(**user.dict())
        self.session.add(new_user)
        await self.session.commit()
        return new_user
