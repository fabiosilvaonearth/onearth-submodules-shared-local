from src.core.generic.services import BaseService
from submodules.shared.src.sys_config.dtos import (
    LookupSysConfig,
    RecordSysConfig,
    ViewSysConfig,
)
from submodules.shared.src.sys_config.entities import SysConfig
from submodules.shared.src.sys_config.repositories import SysConfigRepository


class SysConfigService(
    BaseService[SysConfig, ViewSysConfig, RecordSysConfig, LookupSysConfig]
):
    view_model_cls = ViewSysConfig
    record_model_cls = RecordSysConfig
    lookup_model_cls = LookupSysConfig
    repo_cls = SysConfigRepository
    model_cls = SysConfig
