from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Index,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

from src.core.db.database import Base
from src.core.utils.db import generate_id


class LookupTable(Base):
    __tablename__ = "lookup_tables"
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
    table_name = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "tenant_id",
            "organization_id",
            "table_name",
            name="uq_tenant_lookup_table",
        ),
        Index("ix_tenant_lookup_table", "tenant_id", "organization_id", "table_name"),
    )

    created_by = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_by = Column(UUID(as_uuid=True), nullable=False)
    updated_at = Column(
        DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_by = Column(UUID(as_uuid=True), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True, default=None)


class TenantLookupTableItem(Base):
    __tablename__ = "tenant_lookup_table_items"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=generate_id,
        unique=True,
        index=True,
    )
    lookup_table_id = Column(
        UUID(as_uuid=True), ForeignKey("lookup_tables.id"), nullable=False
    )
    value = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "lookup_table_id",
            "value",
            name="uq_tenant_lookup_table_item",
        ),
        Index("ix_tenant_lookup_table_item", "lookup_table_id", "value"),
    )
