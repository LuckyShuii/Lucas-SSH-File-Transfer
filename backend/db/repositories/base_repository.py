from typing import Type, TypeVar, List, Union
from fastapi import HTTPException, status
from db.models.base_model import Base 
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository:
    def __init__(self, entity_class: Type[ModelType], session: Session):
        self.entity_class = entity_class
        self.session = session
        self.session.expire_on_commit = False

    def read_all(self) -> List[ModelType]:
        return self.session.query(self.entity_class).all()

    def get_by_id(self, id: Union[int, str]) -> Union[ModelType, None]:
        return self.session.query(self.entity_class).filter(self.entity_class.id == id).first()

    def get_all_by(self, *filters) -> List[ModelType]:
        return self.session.query(self.entity_class).filter(*filters).all()

    def get_one_by(self, *filters) -> Union[ModelType, None]:
        return self.session.query(self.entity_class).filter(*filters).first()
