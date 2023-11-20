import httpx

from config.settings import Settings


class ShopifyClient:
    client = httpx.AsyncClient()

    def __init__(
        self,
        shop: str,
        settings: Settings,
        access_token: str | None = None,
    ) -> None:
        self.shop = shop
        self.settings = settings
        if access_token:
            self.access_token = access_token

    @property
    def access_token(self) -> str | None:
        return self.client.headers.get("X-Shopify-Access-Token")

    @access_token.setter
    def access_token(self, value: str):
        self.client.headers["X-Shopify-Access-Token"] = value

    async def auth(self, code: str) -> None:
        if not self.access_token:
            response = await self.client.post(
                f"https://{self.shop}/admin/oauth/access_token",
                data={
                    "client_id": self.settings.shopify_client_id,
                    "client_secret": self.settings.shopify_client_secret,
                    "code": code,
                    "grant_type": "authorization_code",
                    "redirect_uri": self.settings.shopify_redirect_uri,
                },
            )
            response.raise_for_status()
            if response.status_code == 200:
                access_token = response.json()["access_token"]
                self.access_token = access_token

        if not self.access_token:
            raise Exception("No access token")

    async def products(self) -> httpx.Response:
        return await self.client.get(f"https://{self.shop}/admin/products.json")
