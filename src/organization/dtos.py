from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
import uuid
from typing import List, Optional
from enum import Enum
from src.core.utils.appbasemodel import AppBaseModel

class SharedOrganizationEnum(str, Enum):
    _SUMMARY = "_summary"
    _LIGHT = "_light"
    _FULL = "_full"

class RecordOrganizationSegment(AppBaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "organization_id": "123e4567-e89b-12d3-a456-426614174000",
                "segment_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        }
    )
    id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Unique identifier for the organization-segment association',
            'isrequired': True
        }
    )
    organization_id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Identifier for the associated organization',
            'isrequired': True,
            'foreignkey': 'organization'
        }
    )
    segment_id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Identifier for the associated segment',
            'isrequired': True,
            'foreignkey': 'segment'
        }
    )

class RecordOrganizationUser(AppBaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "organization_id": "123e4567-e89b-12d3-a456-426614174000",
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "role_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        }
    )
    id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Unique identifier for the organization-user association',
            'isrequired': True
        }
    )
    organization_id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Identifier for the associated organization',
            'isrequired': True,
            'foreignkey': 'organization'
        }
    )
    user_id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Identifier for the associated user',
            'isrequired': True,
            'foreignkey': 'user'
        }
    )
    role_id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Identifier for the associated role',
            'isrequired': True,
            'foreignkey': 'role'
        }
    )

class RecordSharedOrganization(AppBaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "tenant_id": "123e4567-e89b-12d3-a456-426614174000",
                "organization_id": "123e4567-e89b-12d3-a456-426614174000",
                "shared_type": "_summary"
            }
        }
    )
    id: uuid.UUID
    tenant_id: uuid.UUID
    organization_id: uuid.UUID
    shared_type: SharedOrganizationEnum

class RecordOrganization(AppBaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Acme Corp",
                "tenant_owner_id": "123e4567-e89b-12d3-a456-426614174000",
                "region_id": "123e4567-e89b-12d3-a456-426614174000",
                "segments": [
                    {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "organization_id": "123e4567-e89b-12d3-a456-426614174000",
                        "segment_id": "123e4567-e89b-12d3-a456-426614174000"
                    }
                ],
                "users": [
                    {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "organization_id": "123e4567-e89b-12d3-a456-426614174000",
                        "user_id": "123e4567-e89b-12d3-a456-426614174000",
                        "role_id": "123e4567-e89b-12d3-a456-426614174000"
                    }
                ],
                "shared_organizations": [
                    {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "tenant_id": "123e4567-e89b-12d3-a456-426614174000",
                        "organization_id": "123e4567-e89b-12d3-a456-426614174000",
                        "shared_type": "_summary"
                    }
                ]
            }
        }
    )
    id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Unique identifier for the organization',
            'isrequired': True
        }   
    )
    name: str = Field(
        ...,
        max_length=255,
        json_schema_extra={
            'hint': 'Name of the organization',
            'isrequired': True
        }
    )
    tenant_owner_id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Identifier for the tenant owner',
            'isrequired': True
        }
    )
    region_id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Identifier for the region',
            'isrequired': True
        }
    )
    segments: List[RecordOrganizationSegment] = Field(
        default=[],
        json_schema_extra={
            'hint': 'List of segments associated with the organization'
        }
    )
    users: List[RecordOrganizationUser] = Field(
        default=[],
        json_schema_extra={
            'hint': 'List of users associated with the organization'
        }
    )
    shared_organizations: List[RecordSharedOrganization] = Field(
        default=[],
        json_schema_extra={
            'hint': 'List of shared organizations'
        }
    )

class ViewOrganization(AppBaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Unique identifier for the organization',
            'isrequired': True
        }
    )
    name: str = Field(
        ...,
        max_length=255,
        json_schema_extra={
            'hint': 'Name of the organization',
            'isrequired': True
        }
    )
    region_name: Optional[str] = Field(
        None,
        json_schema_extra={
            'hint': 'Name of the region',
            'isrequired': False
        }
    )
    tenant_name: Optional[str] = Field(
        None,
        json_schema_extra={
            'hint': 'Name of the tenant',
            'isrequired': False
        }
    )

class LookupOrganization(AppBaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: uuid.UUID = Field(
        ...,
        json_schema_extra={
            'hint': 'Unique identifier for the organization',
            'isrequired': True
        }
    )
    name: str = Field(
        ...,
        max_length=255,
        json_schema_extra={
            'hint': 'Name of the organization',
            'isrequired': True,
            'lookupvalue': True
        }
    )
    region_name: Optional[str] = Field(
        None,
        json_schema_extra={
            'hint': 'Name of the region',
            'isrequired': False
        }
    )
    tenant_name: Optional[str] = Field(
        None,
        json_schema_extra={
            'hint': 'Name of the tenant',
            'isrequired': False
        }
    )
