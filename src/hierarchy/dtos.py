import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ViewHierarchy(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "name": "Hierarchy Example",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the Hierarchy",
            "isrequired": True,
        },
    )
    name: str = Field(
        ...,
        example="Hierarchy ABC",
        json_schema_extra={
            "hint": "Name of the Hierarchy",
            "isrequired": True,
        },
    )


class RecordHierarchy(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "tenant_id": "f1e2d3c4-b5a6-7890-abcd-1234567890ef",
                "hierarchy_level_id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Hierarchy Example",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the Hierarchy",
            "isrequired": True,
        },
    )
    tenant_id: uuid.UUID = Field(
        ..., json_schema_extra={"hint": "Identifier for the tenant", "isrequired": True}
    )
    hierarchy_level_id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            "hint": "Identifier for the hierarchy level",
            "isrequired": True,
        },
    )
    name: str = Field(
        ...,
        example="Hierarchy ABC",
        json_schema_extra={
            "hint": "Name of the Hierarchy",
            "isrequired": True,
        },
    )
    enable: bool = Field(
        default=True,
        json_schema_extra={
            "hint": "Indicates if the Hierarchy is enabled",
            "isrequired": False,
        },
    )
    start_data: datetime | None = Field(
        default=None,
        json_schema_extra={
            "hint": "Start date of the Hierarchy",
            "isrequired": False,
        },
    )
    end_date: datetime | None = Field(
        default=None,
        json_schema_extra={
            "hint": "End date of the Hierarchy",
            "isrequired": False,
        },
    )


class LookupHierarchy(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "name": "Hierarchy Example",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the Hierarchy",
            "isrequired": True,
        },
    )
    name: str = Field(
        ...,
        example="Hierarchy ABC",
        json_schema_extra={
            "hint": "Name of the Hierarchy",
            "isrequired": True,
            "lookupvalue": True,
        },
    )
