from fastapi import APIRouter
from src.core.generic.controllers import build_crud_router
from submodules.shared.src.organization.services import OrganizationService

router: APIRouter = build_crud_router(
    resource="organizations",
    service_cls=OrganizationService
)
