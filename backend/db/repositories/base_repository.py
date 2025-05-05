from typing import Type, TypeVar, List, Union
from fastapi import HTTPException, status
from db.models.base_model import Base
from sqlalchemy_pydantic_orm import ORMBaseSchema

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository:
    def __init__(
        self,
        entity_class: Type[Base],
        create_schema: Type[ORMBaseSchema] = None,
        patch_schema: Type[ORMBaseSchema] = None,
        session=None,
    ):
        self.entity_class = entity_class
        self.create_schema = create_schema
        self.patch_schema = patch_schema
        self.session = session

    async def read_all(self):
        items = self.session.query(self.entity_class).all()
        return items

    async def get(self, id: Union[str, int]):
        return await self.get_by(self.entity_class.id == id)

    async def get_or_create(self, entity, **kwargs):
        instance = (
            self.session.query(self.entity_class).filter_by(**kwargs).one_or_none()
        )
        if instance:
            return instance
        else:
            return await self.create(entity)

    async def create(self, entity: Base):
        model_db = entity
        if isinstance(entity, ORMBaseSchema):
            obj_in_cleaned = entity.dict(exclude_unset=True)
            create_schema = self.create_schema.parse_obj(obj_in_cleaned)
            model_db = create_schema.orm_create()
        self.session.add(model_db)
        self.session.commit()
        self.session.refresh(model_db)
        return model_db

    async def delete(self, id: Union[str, int]):
        return await self.delete_by(self.entity_class.id == id)

    async def delete_by(self, *filters):
        obj = await self.get_by(*filters)
        if obj:
            self.session.delete(obj)
            self.session.commit()
        return None

    async def patch_where(self, entity: Base, *filters):
        schema = entity
        if not isinstance(entity, ORMBaseSchema) and self.patch_schema is not None:
            schema = self.patch_schema.from_orm(entity)

        if isinstance(schema, ORMBaseSchema):
            model = await self.get_by(*filters)
            schema.orm_update(self.session, model)
        else:
            model = entity

        self.session.commit()
        self.session.refresh(model)
        return model

    async def patch(self, entity: Base):
        return await self.patch_where(entity, self.entity_class.id == entity.id)

    async def get_by(self, *filters, order=None, raise_error=True):
        query = self.session.query(self.entity_class).filter(*filters)

        if order is not None:
            query = query.order_by(order)

        item = query.limit(1).one_or_none()

        if not item and raise_error:
            return False
        return item

    async def get_all_by(self, *filters):
        items = self.session.query(self.entity_class).filter(*filters).all()
        return items