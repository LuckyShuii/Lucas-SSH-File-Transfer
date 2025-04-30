from typing import Type

from fastapi import Depends

from database import Database
from db.repositories.base_repository import BaseRepository

class BaseManager:
    repository_type: Type[BaseRepository] = None

    def __init__(self, db = None, repository = None):
        self.db = db
        self.repository: BaseRepository = repository

    def __call__(self, db=Depends(Database.get_session)):
        self.db = db
        if self.__class__.repository_type:
            self.repository = self.__class__.repository_type(self.db)
        return self

    def __init_subclass__(cls, repository=None) -> None:
        cls.repository_type = repository