from src.core.generic.repositories import SQLAlchemyRepository
from submodules.shared.src.hierarchy.entities import Hierarchy


class HierarchyRepository(SQLAlchemyRepository[Hierarchy]):
    model_cls = Hierarchy

    def _internal_read(self):
        stmt = super()._internal_read()
        return stmt

    def _internal_view(self):
        stmt = super()._internal_view()
        return stmt
