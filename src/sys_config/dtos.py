import uuid
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, Json


class ViewSysConfig(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "data": "{'key': 'value'}",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the SysConfig",
            "isrequired": True,
        },
    )
    data: Json[dict[str, Any]] = Field(
        ...,
        example="{'key': 'value'}",
        json_schema_extra={
            "hint": "Configuration data in JSON format",
            "isrequired": True,
        },
    )


class RecordSysConfig(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "data": "{'key': 'value'}",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the SysConfig",
            "isrequired": True,
        },
    )
    data: Json[dict[str, Any]] = Field(
        ...,
        example="{'key': 'value'}",
        json_schema_extra={
            "hint": "Configuration data in JSON format",
            "isrequired": True,
        },
    )


class LookupSysConfig(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "data": "{'key': 'value'}",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the SysConfig",
            "isrequired": True,
        },
    )
    data: Json[dict[str, Any]] = Field(
        ...,
        example="{'key': 'value'}",
        json_schema_extra={
            "hint": "Configuration data in JSON format",
            "isrequired": True,
            "lookupvalue": False,
        },
    )
