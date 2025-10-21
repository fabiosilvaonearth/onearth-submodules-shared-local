from fastapi import APIRouter

from src.core.generic.controllers import build_crud_router
from submodules.shared.src.hierarchy.services import HierarchyService

router: APIRouter = build_crud_router(
    resource="hierarchies", service_cls=HierarchyService
)
