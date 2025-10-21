from sqlalchemy.orm import joinedload, selectinload
from src.core.generic.repositories import SQLAlchemyRepository
from submodules.shared.src.segments.entities import Segment

class SegmentRepository(SQLAlchemyRepository[Segment]):
    model_cls = Segment

    def _internal_read(self):
        stmt = super()._internal_read()
        return stmt

    def _internal_view(self):
        stmt = super()._internal_view()
        return stmt

