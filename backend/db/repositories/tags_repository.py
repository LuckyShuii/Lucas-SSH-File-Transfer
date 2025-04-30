from db.repositories.base_repository import BaseRepository
from db.models.tags_model import Tags
from sqlalchemy.orm import Session

class TagsRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(Tags, session)

    def read_all(self):
        return super().read_all()

    def read_by_name(self, name: str):
        return self.get_one_by(Tags.name == name)
