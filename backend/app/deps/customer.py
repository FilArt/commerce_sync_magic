from fastapi import Header, HTTPException
from app.models.customer import Customer


async def get_current_customer(
    shopify_token: str = Header(alias="X-Shopify-Access-Token")
):
    print(shopify_token)
    if shopify_token:
        return Customer(shopify_id=shopify_token)
    else:
        raise HTTPException(status_code=401, detail="Invalid token")
