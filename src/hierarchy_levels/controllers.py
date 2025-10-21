from fastapi import APIRouter

from src.core.generic.controllers import build_crud_router
from submodules.shared.src.hierarchy_levels.services import HierarchyLevelService

router: APIRouter = build_crud_router(
    resource="hierarchy-levels", service_cls=HierarchyLevelService
)
