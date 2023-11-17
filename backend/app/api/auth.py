from fastapi import APIRouter, Depends
from app.deps.auth import get_shopify_auth_url

auth_router = APIRouter()


@auth_router.post("/shopify_auth_url", response_model=str)
async def shopify(shopify_auth_url: str = Depends(get_shopify_auth_url)):
    return shopify_auth_url
