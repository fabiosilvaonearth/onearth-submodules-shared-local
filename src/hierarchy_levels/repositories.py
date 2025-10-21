from src.core.generic.repositories import SQLAlchemyRepository
from submodules.shared.src.hierarchy_levels.entities import HierarchyLevel


class HierarchyLevelRepository(SQLAlchemyRepository[HierarchyLevel]):
    model_cls = HierarchyLevel

    def _internal_read(self):
        stmt = super()._internal_read()
        return stmt

    def _internal_view(self):
        stmt = super()._internal_view()
        return stmt
