from db.schemas.base_schema import BaseSchema
from pydantic import PrivateAttr, Field
from db.models.user_model import User

class UserBase(BaseSchema):
    username: str   
    email: str
    password: str

    _orm_model: User = PrivateAttr(default=User)
    
class UserSchema(UserBase):
    role: str = Field(default="user")
    is_activated: int = Field(default=0)
    id: int
    uuid: str
    created_at: str
    updated_at: str

class UserCreate(UserBase):
    rgpd: bool = Field(default=False)