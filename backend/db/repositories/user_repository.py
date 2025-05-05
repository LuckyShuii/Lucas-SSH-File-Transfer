from db.repositories.base_repository import BaseRepository
from db.models.user_model import User
from sqlalchemy.orm import Session

class UserRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(entity_class=User, session=session)

    async def read_all(self):
        return await super().read_all()

    async def read_by_username(self, name: str):
        return await self.get_by(User.username == name)
