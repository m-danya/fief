from typing import Any, Dict, List, Tuple, Type

import pycountry
from fastapi import Depends
from pydantic import ValidationError

from fief.dependencies.form import get_form_data_dict
from fief.dependencies.locale import get_translations
from fief.dependencies.tenant import get_current_tenant
from fief.dependencies.user_field import (
    get_registration_user_fields,
    get_user_create_model,
)
from fief.exceptions import FormValidationError
from fief.locale import Translations
from fief.models import Tenant, UserField
from fief.schemas.user import UC


async def get_register_context(
    registration_user_fields: List[UserField] = Depends(get_registration_user_fields),
    tenant: Tenant = Depends(get_current_tenant),
) -> Dict[str, Any]:
    countries: List[Tuple[str, str]] = [
        (country.alpha_2, country.name) for country in pycountry.countries
    ]
    return {
        "tenant": tenant,
        "registration_user_fields": registration_user_fields,
        "countries": countries,
    }


async def get_user_create(
    form_data_dict: Dict[str, Any] = Depends(get_form_data_dict),
    user_create_model: Type[UC] = Depends(get_user_create_model),
    register_context: Dict[str, Any] = Depends(get_register_context),
    translations: Translations = Depends(get_translations),
) -> UC:
    try:
        return user_create_model(**form_data_dict)
    except ValidationError as e:
        raise FormValidationError(
            "register.html",
            {
                "form_data": form_data_dict,
                **register_context,
            },
            translations,
            e.raw_errors,
            user_create_model,
        ) from e
