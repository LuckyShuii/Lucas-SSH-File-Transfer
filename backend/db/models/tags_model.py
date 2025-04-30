from .base_model import Base
from sqlalchemy import Column, String, Integer
import uuid

class Tags(Base):
    __tablename__ = "tags"

    uuid = Column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False, primary_key=True)
    name = Column(String(255), nullable=False)
    icon_name = Column(String(100), nullable=False)
    background_color = Column(String(20), nullable=False)
