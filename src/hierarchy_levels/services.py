from src.core.generic.services import BaseService
from submodules.shared.src.hierarchy_levels.dtos import (
    LookupHierarchyLevel,
    RecordHierarchyLevel,
    ViewHierarchyLevel,
)
from submodules.shared.src.hierarchy_levels.entities import HierarchyLevel
from submodules.shared.src.hierarchy_levels.repositories import HierarchyLevelRepository


class HierarchyLevelService(
    BaseService[
        HierarchyLevel, ViewHierarchyLevel, RecordHierarchyLevel, LookupHierarchyLevel
    ]
):
    view_model_cls = ViewHierarchyLevel
    record_model_cls = RecordHierarchyLevel
    lookup_model_cls = LookupHierarchyLevel
    repo_cls = HierarchyLevelRepository
    model_cls = HierarchyLevel
