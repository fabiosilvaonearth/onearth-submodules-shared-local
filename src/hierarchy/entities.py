from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Index,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

from src.core.db.database import Base
from src.core.utils.db import generate_id
from submodules.shared.src.enums import HierarchyRelationType


class Hierarchy(Base):
    __tablename__ = "hierarchies"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=generate_id,
        unique=True,
        index=True,
    )
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    hierarchy_level_id = Column(
        UUID(as_uuid=True), ForeignKey("hierarchy_levels.id"), nullable=False
    )
    name = Column(String, nullable=False)
    enable = Column(Boolean, nullable=False, default=True)
    start_date = Column(DateTime(timezone=True), nullable=True)
    end_date = Column(DateTime(timezone=True), nullable=True)

    __table_args__ = (
        UniqueConstraint(
            "tenant_id",
            "hierarchy_level_id",
            "name",
            name="uq_tenant_hierarchies",
        ),
        Index("ix_tenant_hierarchies", "tenant_id", "hierarchy_level_id", "name"),
    )

    created_by = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_by = Column(UUID(as_uuid=True), nullable=False)
    updated_at = Column(
        DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_by = Column(UUID(as_uuid=True), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True, default=None)


class HierarchyRelation(Base):
    __tablename__ = "hierarchy_relations"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=generate_id,
        unique=True,
        index=True,
    )
    parent_id = Column(UUID(as_uuid=True), ForeignKey("hierarchies.id"), nullable=False)
    child_id = Column(UUID(as_uuid=True), ForeignKey("hierarchies.id"), nullable=False)
    hierarchy_relation_type = Column(
        Enum(
            HierarchyRelationType,
            name="hierarchy_relation_types",
            native_enum=True,
        ),
        nullable=False,
    )

    __table_args__ = (
        UniqueConstraint(
            "parent_id",
            "child_id",
            name="uq_hierarchy_relations",
        ),
        Index("ix_hierarchy_relations", "parent_id", "child_id"),
    )
