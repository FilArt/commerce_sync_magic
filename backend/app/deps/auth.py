from typing import Annotated
from app.deps.settings import get_settings
from config.settings import Settings
from fastapi import Depends, Body


def get_shopify_auth_url(
    shop: Annotated[str, Body(embed=True)], settings: Settings = Depends(get_settings)
) -> str:
    return f"https://{shop}/admin/oauth/authorize?client_id={settings.shopify_client_id}&scope={settings.shopify_scope}&redirect_uri={settings.shopify_redirect_uri}"
