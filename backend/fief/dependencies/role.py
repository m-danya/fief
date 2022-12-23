from fastapi import Depends, HTTPException, Query, status
from pydantic import UUID4
from sqlalchemy import select

from fief.dependencies.pagination import (
    GetPaginatedObjects,
    Ordering,
    PaginatedObjects,
    Pagination,
    get_ordering,
    get_paginated_objects_getter,
    get_pagination,
)
from fief.dependencies.workspace_repositories import get_workspace_repository
from fief.models import Role
from fief.repositories import RoleRepository


async def get_paginated_roles(
    query: str | None = Query(None),
    pagination: Pagination = Depends(get_pagination),
    ordering: Ordering = Depends(get_ordering),
    repository: RoleRepository = Depends(get_workspace_repository(RoleRepository)),
    get_paginated_objects: GetPaginatedObjects[Role] = Depends(
        get_paginated_objects_getter
    ),
) -> PaginatedObjects[Role]:
    statement = select(Role)

    if query is not None:
        statement = statement.where(Role.name.ilike(f"%{query}%"))

    return await get_paginated_objects(statement, pagination, ordering, repository)


async def get_role_by_id_or_404(
    id: UUID4,
    repository: RoleRepository = Depends(get_workspace_repository(RoleRepository)),
) -> Role:
    role = await repository.get_by_id(id)

    if role is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return role
