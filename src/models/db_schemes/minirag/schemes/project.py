from .minirag_base import SQLAlchemyBase
from sqlalchemy import Column , Integar , DateTime , func
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Project(SQLAlchemyBase):

    __tablename__ = "projects"
    project_id = Column(Integar , primary_key = True , autoincrement = True)
    project_uuid = Column(UUID(as_uuid = True), default = uuid.uuid4, unique = True , nullable = False)

    created_at = Column(DateTime(timezone = True), server_default = func.now() , nullable = True)
    updated_at = Column(DateTime(timezone = True), onupdate = func.now() , nullable = False)