from .base_model import Base
from sqlalchemy import Column, String, Integer
import uuid

class User(Base):
    __tablename__ = "user"

    uuid = Column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)

    # @is_activated is a boolean field that indicates whether the user has activated their account or not via email
    # 0 = not activated, 1 = activated
    is_activated = Column(Integer, default=0)
    role = Column(String(20), default="user")
    created_at = Column(String(50), nullable=False, default="CURRENT_TIMESTAMP")
    updated_at = Column(String(50), nullable=False, default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")   
