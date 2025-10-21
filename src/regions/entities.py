import uuid
from sqlalchemy import Column, String, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from src.core.db.database import Base
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from src.core.utils.db import generate_id

class Region(Base):
    __tablename__ = "regions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_id, unique=True, index=True)
    name = Column(String)
    parent_id = Column(UUID(as_uuid=True), ForeignKey("regions.id"), nullable=True)
    parent = relationship("Region", remote_side=[id],backref="children")
    created_by = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_by = Column(UUID(as_uuid=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now())
    deleted_by = Column(UUID(as_uuid=True), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True, default=None)
