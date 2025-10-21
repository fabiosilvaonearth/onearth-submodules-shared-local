from sqlalchemy import (
    JSON,
    Column,
    DateTime,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

from src.core.db.database import Base
from src.core.utils.db import generate_id


class SysConfig(Base):
    __tablename__ = "sys_configs"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=generate_id,
        unique=True,
        index=True,
    )
    data = Column(JSON, nullable=False)

    created_by = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_by = Column(UUID(as_uuid=True), nullable=False)
    updated_at = Column(
        DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now()
    )
    deleted_by = Column(UUID(as_uuid=True), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True, default=None)
