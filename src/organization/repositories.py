from sqlalchemy.orm import joinedload, selectinload
from src.base.role.entities import Role
from src.base.user.entities import User
from src.core.generic.repositories import SQLAlchemyRepository
from submodules.shared.src.organization.entities import Organization

class OrganizationRepository(SQLAlchemyRepository[Organization]):
    model_cls = Organization

    def _internal_read(self):
        stmt = super()._internal_read()
        # stmt = stmt.options(
        #     selectinload(Organization.organization_users).options(
        #         selectinload(OrganizationUsers.user).load_only(User.name),
        #         selectinload(OrganizationUsers.role).load_only(Role.name)
        #     )
        # )
        return stmt

    def _internal_view(self):
        stmt = super()._internal_view()
        return stmt

