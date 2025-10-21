from src.core.generic.repositories import SQLAlchemyRepository
from submodules.shared.src.sys_config.entities import SysConfig


class SysConfigRepository(SQLAlchemyRepository[SysConfig]):
    model_cls = SysConfig

    def _internal_read(self):
        stmt = super()._internal_read()
        return stmt

    def _internal_view(self):
        stmt = super()._internal_view()
        return stmt
