from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime, func
from src.core.db.database import Base
from src.core.utils.db import generate_id

class Segment(Base):
    __tablename__ = "segments"
    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_id, unique=True, index=True)
    name = Column(String)
    created_by = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_by = Column(UUID(as_uuid=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now())
    deleted_by = Column(UUID(as_uuid=True), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True, default=None)
