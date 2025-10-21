from src.core.generic.services import BaseService
from submodules.shared.src.hierarchy.dtos import (
    LookupHierarchy,
    RecordHierarchy,
    ViewHierarchy,
)
from submodules.shared.src.hierarchy.entities import Hierarchy
from submodules.shared.src.hierarchy.repositories import HierarchyRepository


class HierarchyService(
    BaseService[Hierarchy, ViewHierarchy, RecordHierarchy, LookupHierarchy]
):
    view_model_cls = ViewHierarchy
    record_model_cls = RecordHierarchy
    lookup_model_cls = LookupHierarchy
    repo_cls = HierarchyRepository
    model_cls = Hierarchy
