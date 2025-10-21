from fastapi import APIRouter

from src.core.generic.controllers import build_crud_router
from submodules.shared.src.lookup_tables.services import LookupTableService

router: APIRouter = build_crud_router(
    resource="lookup-tables", service_cls=LookupTableService
)
