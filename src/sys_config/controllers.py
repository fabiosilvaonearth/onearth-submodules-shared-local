from fastapi import APIRouter

from src.core.generic.controllers import build_crud_router
from submodules.shared.src.sys_config.services import SysConfigService

router: APIRouter = build_crud_router(
    resource="sysconfig", service_cls=SysConfigService
)
