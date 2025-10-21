from src.core.generic.services import BaseService
from submodules.shared.src.regions.entities import Region
from submodules.shared.src.regions.dtos import RecordRegion, ViewRegion, LookupRegion
from submodules.shared.src.regions.repositories import RegionRepository

class RegionService(BaseService[Region, ViewRegion, RecordRegion, LookupRegion]):
    view_model_cls = ViewRegion
    record_model_cls = RecordRegion
    lookup_model_cls = LookupRegion
    repo_cls = RegionRepository
    model_cls = Region
