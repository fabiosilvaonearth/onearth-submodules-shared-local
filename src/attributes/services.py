from src.core.generic.services import BaseService
from submodules.shared.src.attributes.dtos import (
    LookupAttribute,
    RecordAttribute,
    ViewAttribute,
)
from submodules.shared.src.attributes.entities import Attribute
from submodules.shared.src.attributes.repositories import AttributeRepository


class AttributeService(
    BaseService[Attribute, ViewAttribute, RecordAttribute, LookupAttribute]
):
    view_model_cls = ViewAttribute
    record_model_cls = RecordAttribute
    lookup_model_cls = LookupAttribute
    repo_cls = AttributeRepository
    model_cls = Attribute
