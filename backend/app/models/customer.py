from sqlmodel import BINARY, Field, Relationship, SQLModel

__all__ = ["Customer", "ShopifyShop"]


class Customer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    shopify_access_token: bytes | None = Field(default=None, sa_column=BINARY)
    shops: list["ShopifyShop"] = Relationship(back_populates="customer")


class ShopifyShop(SQLModel, table=True):
    name: str = Field(primary_key=True)
    customer: Customer = Relationship(back_populates="shops")
    customer_id: int = Field(foreign_key="customer.id")
