from sqlalchemy.orm import joinedload, selectinload
from src.core.generic.repositories import SQLAlchemyRepository
from submodules.shared.src.regions.entities import Region

class RegionRepository(SQLAlchemyRepository[Region]):
    model_cls = Region

    def _internal_read(self):
        stmt = super()._internal_read()
        return stmt

    def _internal_view(self):
        stmt = super()._internal_view()
        return stmt
