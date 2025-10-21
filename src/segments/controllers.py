from fastapi import APIRouter
from src.core.generic.controllers import build_crud_router
from submodules.shared.src.segments.services import SegmentService

router: APIRouter = build_crud_router(
    resource="segments",
    service_cls=SegmentService
)
