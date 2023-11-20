from typing import Annotated
from config.settings import Settings, get_settings
from fastapi import Depends, Body


def get_shopify_auth_url(
    shop: Annotated[str, Body(embed=True)], settings: Settings = Depends(get_settings)
) -> str:
    base_url = "https://{shop}.myshopify.com/admin/oauth/authorize?client_id={client_id}&scope={scopes}&redirect_uri={redirect_uri}&state={nonce}&grant_options[]={access_mode}"
    return base_url.format(
        shop=shop,
        client_id=settings.shopify_client_id,
        scopes=settings.shopify_scope,
        redirect_uri=settings.shopify_redirect_uri,
        nonce="",
        access_mode="offline",
    )
