import uuid
from enum import Enum as PyEnum
from sqlalchemy import DateTime, func
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from sqlalchemy import Column, ForeignKey, String, Enum
from sqlalchemy.dialects.postgresql import UUID
from src.core.db.database import Base
from src.core.utils.db import generate_id

class SharedEnum(PyEnum):
    _SUMMARY = "_summary"
    _LIGHT = "_light"
    _FULL = "_full"

class Organization(Base):
    __tablename__ = "organizations"
    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_id, unique=True, index=True)
    name = Column(String, nullable=False)
    tenant_owner_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    region_id = Column(UUID(as_uuid=True),ForeignKey("regions.id"), nullable=False)
    region = relationship("Region", backref="organizations")
    tenant = relationship("Tenant",backref="organizations")
    created_by = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_by = Column(UUID(as_uuid=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now())
    deleted_by = Column(UUID(as_uuid=True), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True, default=None)

class OrganizationSegment(Base):
    __tablename__ = "organization_segments" 
    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_id, unique=True, index=True)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False)
    segment_id = Column(UUID(as_uuid=True), ForeignKey("segments.id"), nullable=False)
    organization = relationship("Organization", backref="organization_segments")
    segment = relationship("Segment", backref="organization_segments")

class OrganizationUser(Base):
    __tablename__ = "organization_users" 
    id = Column(UUID(as_uuid=True),primary_key=True,default=generate_id, unique=True, index=True)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"), nullable=False)
    organization = relationship("Organization", backref="organization_users")
    user = relationship("User")
    role = relationship("Role")

class SharedOrganization(Base):
    __tablename__ = "shared_organizations"
    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_id, unique=True, index=True)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    shared_type = Column(Enum(SharedEnum),nullable=False)
    organization = relationship("Organization", backref="shared_organizations")
    tenant = relationship("Tenant",backref="shared_organizations")
