from typing import Annotated
from fastapi import APIRouter, Body, Depends
from sqlmodel import Session, select
from app.deps.shopify import ShopifyClient
from app.deps.auth import get_shopify_auth_url
from app.db import get_session
from app.models import Customer, ShopifyShop
from cryptography.fernet import Fernet

from config.settings import Settings, get_settings


auth_router = APIRouter()


@auth_router.post("/shopify_auth_url", response_model=str)
async def shopify(shopify_auth_url: str = Depends(get_shopify_auth_url)):
    return shopify_auth_url


def shop_param(shop: Annotated[str, Body(embed=True)]):
    if not shop.endswith(".myshopify.com"):
        shop += ".myshopify.com"
    if shop.startswith("https://"):
        shop = shop[8:]
    return shop


@auth_router.post("/shopify_callback")
async def shopify_callback(
    code: Annotated[str, Body(embed=True)],
    shop: Annotated[str, Depends(shop_param)],
    session: Session = Depends(get_session),
    settings: Settings = Depends(get_settings),
) -> list[ShopifyShop]:
    shopify_client = ShopifyClient(shop=shop, settings=settings)
    await shopify_client.auth(code)

    f = Fernet(settings.secret_key)
    encrypted_access_token = f.encrypt(shopify_client.access_token.encode())
    db_customer = session.exec(
        select(Customer).where(Customer.shopify_access_token == encrypted_access_token)
    ).first()
    if db_customer is None:
        db_customer = Customer(shopify_access_token=encrypted_access_token)
        session.add(db_customer)
        session.commit()
        session.refresh(db_customer)

    db_shop = session.exec(
        select(ShopifyShop).where(
            ShopifyShop.customer == db_customer
            and ShopifyShop.name == shopify_client.shop
        )
    ).first()
    if db_shop is None:
        db_shop = ShopifyShop(customer_id=db_customer.id, name=shopify_client.shop)
        session.add(db_shop)
        session.commit()
        session.refresh(db_shop)

    return db_customer.shops
