from src.core.generic.repositories import SQLAlchemyRepository
from submodules.shared.src.attributes.entities import Attribute


class AttributeRepository(SQLAlchemyRepository[Attribute]):
    model_cls = Attribute

    def _internal_read(self):
        stmt = super()._internal_read()
        return stmt

    def _internal_view(self):
        stmt = super()._internal_view()
        return stmt
