from functools import lru_cache
from pydantic.env_settings import BaseSettings


class Settings(BaseSettings):
    # shopify
    shopify_client_id: str = "test"
    shopify_client_secret: str = "test"
    shopify_scope: str = "read_products,write_products"
    shopify_redirect_uri: str = "http://localhost:3000/auth"

    secret_key: bytes = b"test"


settings = Settings()


@lru_cache
def get_settings():
    return Settings()
