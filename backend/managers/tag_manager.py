from managers.base_manager import BaseManager
from db.repositories.tags_repository import TagRepository
from db.schemas.tags_schema import TagCreate, TagPatch
from db.models.tags_model import Tags
from fastapi import HTTPException, status

class TagManager(BaseManager, repository=TagRepository):
    async def all_tags(self) -> Tags:
        return await self.repository.read_all()

    async def get_tag_by_name(self, tag_name: str) -> Tags:
        return await self.repository.read_by_name(tag_name)
