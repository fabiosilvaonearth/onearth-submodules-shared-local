import uuid

from pydantic import BaseModel, ConfigDict, Field


class ViewHierarchyLevel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "name": "HierarchyLevel Example",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the HierarchyLevel",
            "isrequired": True,
        },
    )
    name: str = Field(
        ...,
        example="HierarchyLevel ABC",
        json_schema_extra={
            "hint": "Name of the HierarchyLevel",
            "isrequired": True,
        },
    )


class RecordHierarchyLevel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "name": "HierarchyLevel Example",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the HierarchyLevel",
            "isrequired": True,
        },
    )
    tenant_id: uuid.UUID = Field(
        ..., json_schema_extra={"hint": "Identifier for the tenant", "isrequired": True}
    )
    level: int = Field(
        ...,
        example="1",
        json_schema_extra={
            "hint": "Number of the HierarchyLevel",
            "isrequired": True,
        },
    )
    name: str = Field(
        ...,
        example="HierarchyLevel ABC",
        json_schema_extra={
            "hint": "Name of the HierarchyLevel",
            "isrequired": True,
        },
    )


class LookupHierarchyLevel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
                "name": "HierarchyLevel Example",
            }
        },
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            "hint": "Unique identifier for the HierarchyLevel",
            "isrequired": True,
        },
    )
    name: str = Field(
        ...,
        example="HierarchyLevel ABC",
        json_schema_extra={
            "hint": "Name of the HierarchyLevel",
            "isrequired": True,
            "lookupvalue": True,
        },
    )
