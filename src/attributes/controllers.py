from fastapi import APIRouter

from src.core.generic.controllers import build_crud_router
from submodules.shared.src.attributes.services import AttributeService

router: APIRouter = build_crud_router(
    resource="attributes", service_cls=AttributeService
)
