from pydantic import BaseModel


class Customer(BaseModel):
    shopify_id: str
