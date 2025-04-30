from typing import List, Optional
from pydantic import Field
from db.schemas.base_schema import BaseSchema

class TagSchema(BaseSchema):  # forward ref
    pass

class ProjectSchema(BaseSchema):
    id: int
    uuid: str
    title: str
    description: Optional[str]
    preview_description: Optional[str]
    tags: Optional[List["TagSchema"]] = Field(default_factory=list)

    class Config:
        orm_mode = True
