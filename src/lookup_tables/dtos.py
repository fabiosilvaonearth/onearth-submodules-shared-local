import uuid

from pydantic import BaseModel, ConfigDict, Field


class ViewLookupTable(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "name": "LookupTable Example",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the LookupTable",
            "isrequired": True,
        },
    )
    table_name: str = Field(
        ...,
        example="LookupTable ABC",
        json_schema_extra={
            "hint": "Name of the LookupTable",
            "isrequired": True,
        },
    )


class RecordLookupTable(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "name": "LookupTable Example",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the LookupTable",
            "isrequired": True,
        },
    )
    tenant_id: uuid.UUID = Field(
        ...,
        json_schema_extra={"hint": "Identifier for the tenant", "isrequired": False},
    )
    organization_id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            "hint": "Identifier for the organization",
            "isrequired": False,
        },
    )
    table_name: str = Field(
        ...,
        example="LookupTable ABC",
        json_schema_extra={
            "hint": "Name of the LookupTable",
            "isrequired": True,
        },
    )


class LookupLookupTable(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "name": "LookupTable Example",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the LookupTable",
            "isrequired": True,
        },
    )
    table_name: str = Field(
        ...,
        example="LookupTable ABC",
        json_schema_extra={
            "hint": "Name of the LookupTable",
            "isrequired": True,
            "lookupvalue": True,
        },
    )
