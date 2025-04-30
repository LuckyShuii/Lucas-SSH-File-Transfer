from typing import List, Optional
from pydantic import Field
from db.schemas.base_schema import BaseSchema

class ProjectSchema(BaseSchema):  # forward ref
    pass

class TagSchema(BaseSchema):
    id: int
    uuid: str
    name: str
    icon_name: str
    background_color: str
    projects: Optional[List["ProjectSchema"]] = Field(default_factory=list)

    class Config:
        orm_mode = True
