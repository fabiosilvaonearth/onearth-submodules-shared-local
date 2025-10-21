from src.core.generic.services import BaseService
from submodules.shared.src.lookup_tables.dtos import (
    LookupLookupTable,
    RecordLookupTable,
    ViewLookupTable,
)
from submodules.shared.src.lookup_tables.entities import LookupTable
from submodules.shared.src.lookup_tables.repositories import LookupTableRepository


class LookupTableService(
    BaseService[LookupTable, ViewLookupTable, RecordLookupTable, LookupLookupTable]
):
    view_model_cls = ViewLookupTable
    record_model_cls = RecordLookupTable
    lookup_model_cls = LookupLookupTable
    repo_cls = LookupTableRepository
    model_cls = LookupTable
