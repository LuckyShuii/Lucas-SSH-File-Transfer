from db.repositories.base_repository import BaseRepository
from db.models.projects_model import Projects
from sqlalchemy.orm import Session

class ProjectsRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(Projects, session)

    def read_all(self):
        return super().read_all()

    def read_by_name(self, name: str):
        return self.get_one_by(Projects.name == name)
