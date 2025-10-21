from src.core.generic.repositories import SQLAlchemyRepository
from submodules.shared.src.lookup_tables.entities import LookupTable


class LookupTableRepository(SQLAlchemyRepository[LookupTable]):
    model_cls = LookupTable

    def _internal_read(self):
        stmt = super()._internal_read()
        return stmt

    def _internal_view(self):
        stmt = super()._internal_view()
        return stmt
