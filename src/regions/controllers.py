from fastapi import APIRouter
from src.core.generic.controllers import build_crud_router
from submodules.shared.src.regions.services import RegionService

router: APIRouter = build_crud_router(
    resource="regions",
    service_cls=RegionService
)
