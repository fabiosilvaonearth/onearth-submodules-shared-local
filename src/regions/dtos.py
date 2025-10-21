from __future__ import annotations
from typing import Optional
import uuid
from pydantic import BaseModel, ConfigDict, Field
from src.core.utils.appbasemodel import AppBaseModel

class ViewRegion(AppBaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "North Region"
            }
        }
    )
    id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Unique identifier for the region',
            'isrequired': True
        })
    name: str = Field(
        ...,
        json_schema_extra={
            'hint': 'Name of the region',
            'isrequired': True
        })

class RecordRegion(AppBaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "North Region",
                "parent_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        }
    )
    id: uuid.UUID
    name: str = Field(
        ...,
        max_length=255,
        json_schema_extra={
            'hint': 'Name of the region',
            'isrequired': True
        })
    parent_id: Optional[uuid.UUID] = Field(
        None,
        json_schema_extra={
            'hint': 'Parent region ID',
            'isrequired': False,
            'foreignkey': 'region'
        })

class LookupRegion(AppBaseModel):
    id: Optional[uuid.UUID] = Field(
        None,
        json_schema_extra={
            'hint': 'Unique identifier for the region',
            'isrequired': True
        })
    name: str = Field(
        ...,
        max_length=255,
        json_schema_extra={
            'hint': 'Name of the region',
            'isrequired': True,
            'lookupvalue': True
        })
