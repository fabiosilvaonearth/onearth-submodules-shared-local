from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

from src.core.db.database import Base
from src.core.utils.db import generate_id


class HierarchyLevel(Base):
    __tablename__ = "hierarchy_levels"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=generate_id,
        unique=True,
        index=True,
    )
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    level = Column(Integer, nullable=False)
    name = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "tenant_id",
            "name",
            name="uq_tenant_herarchy_level",
        ),
        Index("ix_tenant_herarchy_level", "tenant_id", "name"),
    )

    created_by = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_by = Column(UUID(as_uuid=True), nullable=False)
    updated_at = Column(
        DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_by = Column(UUID(as_uuid=True), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True, default=None)
