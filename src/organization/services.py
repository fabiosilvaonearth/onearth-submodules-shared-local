from src.core.generic.services import BaseService
from submodules.shared.src.organization.dtos import ViewOrganization, RecordOrganization, LookupOrganization
from submodules.shared.src.organization.entities import Organization
from submodules.shared.src.organization.repositories import OrganizationRepository

class OrganizationService(BaseService[Organization, ViewOrganization, RecordOrganization, LookupOrganization]):
    view_model_cls = ViewOrganization
    record_model_cls = RecordOrganization
    lookup_model_cls = LookupOrganization
    repo_cls = OrganizationRepository
    model_cls = Organization
