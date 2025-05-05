# from sqlalchemy import Table, Column, Integer, ForeignKey
# from .base_model import Base

# projects_tags = Table(
#     "projects_tags",
#     Base.metadata,
#     Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
#     Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
# )
