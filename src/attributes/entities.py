from sqlalchemy import (
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
from submodules.shared.src.enums import FieldType


class Attribute(Base):
    __tablename__ = "attributes"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=generate_id,
        unique=True,
        index=True,
    )
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=True)
    organization_id = Column(
        UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=True
    )
    field_name = Column(String, nullable=False)
    field_type = Column(
        Enum(
            FieldType,
            name="field_types",
            native_enum=True,
        ),
        nullable=False,
    )
    field_mask = Column(String, nullable=True)
    lookup_table_id = Column(
        UUID(as_uuid=True), ForeignKey("lookup_tables.id"), nullable=False
    )

    __table_args__ = (
        UniqueConstraint(
            "tenant_id",
            "organization_id",
            "field_name",
            name="uq_tenant_field_name",
        ),
        Index("ix_tenant_field_name", "tenant_id", "organization_id", "field_name"),
    )

    created_by = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_by = Column(UUID(as_uuid=True), nullable=False)
    updated_at = Column(
        DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_by = Column(UUID(as_uuid=True), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True, default=None)
