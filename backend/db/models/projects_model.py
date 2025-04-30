from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base_model import Base
import uuid

class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), default=str(uuid.uuid4()), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    fr_preview_desciption = Column(String(255))
    en_preview_desciption = Column(String(255))
    fr_description = Column(String)
    en_description = Column(String)
    url = Column(String(255))

    tags = relationship("Tags", secondary="projects_tags", back_populates="projects")
