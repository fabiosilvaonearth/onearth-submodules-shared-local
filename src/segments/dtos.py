from __future__ import annotations
import uuid
from pydantic import BaseModel, ConfigDict, Field
from src.core.utils.appbasemodel import AppBaseModel

class ViewSegment(AppBaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Premium Customers"
            }
        }
    )
    id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Unique identifier for the segment',
            'isrequired': True
        })
    name: str = Field(
        ...,
        max_length=255,
        json_schema_extra={
            'hint': 'Name of the segment',
            'isrequired': True
        })

class RecordSegment(AppBaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Premium Customers"
            }
        }
    )
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        json_schema_extra={
            'hint': 'Unique identifier for the segment',
            'isrequired': True
        })
    name: str = Field(
        ...,
        max_length=255,
        json_schema_extra={
            'hint': 'Name of the segment',
            'isrequired': True
        })

class LookupSegment(AppBaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Premium Customers"
            }
        }
    )
    id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Unique identifier for the segment',
            'isrequired': False
        })
    name: str = Field(
        ...,
        max_length=255,
        json_schema_extra={
            'hint': 'Name of the segment',
            'isrequired': True,
            'lookupvalue': True
        })
