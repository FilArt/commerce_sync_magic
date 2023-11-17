from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    shopify_client_id: str = "test"
    shopify_client_secret: str = "test"
    shopify_scope: str = "test"
    shopify_redirect_uri: str = "test"


settings = Settings()
app = FastAPI()
