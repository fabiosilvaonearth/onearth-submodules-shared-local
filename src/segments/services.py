from src.core.generic.services import BaseService
from submodules.shared.src.segments.entities import Segment
from submodules.shared.src.segments.dtos import RecordSegment, ViewSegment, LookupSegment
from submodules.shared.src.segments.repositories import SegmentRepository

class SegmentService(BaseService[Segment, ViewSegment, RecordSegment, LookupSegment]):
    view_model_cls = ViewSegment
    record_model_cls = RecordSegment
    lookup_model_cls = LookupSegment
    repo_cls = SegmentRepository
    model_cls = Segment
