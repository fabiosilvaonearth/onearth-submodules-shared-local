import uuid

from pydantic import BaseModel, ConfigDict, Field


class ViewAttribute(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "field_name": "Attribute Example",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the Attribute",
            "isrequired": True,
        },
    )
    field_name: str = Field(
        ...,
        example="Attribute ABC",
        json_schema_extra={
            "hint": "Name of the Attribute",
            "isrequired": True,
        },
    )


class RecordAttribute(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "field_name": "Attribute Example",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the Attribute",
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
    field_name: str = Field(
        ...,
        example="Attribute ABC",
        json_schema_extra={
            "hint": "Name of the Attribute",
            "isrequired": True,
        },
    )
    field_type: str = Field(
        ...,
        example="_double",
        json_schema_extra={
            "hint": "Type of the Attribute",
            "isrequired": True,
        },
    )
    field_mask: str = Field(
        ...,
        example="Attribute Mask",
        json_schema_extra={
            "hint": "Mask of the Attribute",
            "isrequired": False,
        },
    )
    lookup_table_id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            "hint": "Identifier for the lookup table",
            "isrequired": False,
        },
    )


class LookupAttribute(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "field_name": "Attribute Example",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the Attribute",
            "isrequired": True,
        },
    )
    field_name: str = Field(
        ...,
        example="Attribute ABC",
        json_schema_extra={
            "hint": "Name of the Attribute",
            "isrequired": True,
            "lookupvalue": True,
        },
    )
