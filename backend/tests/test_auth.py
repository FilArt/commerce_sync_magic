import httpx
from pytest_mock import MockerFixture
from sqlmodel import Session, select
from app.models import Customer


def test_shopify_auth_url(client):
    response = client.post("/api/auth/shopify_auth_url", json={"shop": "test-shop"})
    url = response.json()
    assert (
        url
        == "https://test-shop.myshopify.com/admin/oauth/authorize?client_id=test&scope=read_products,write_products&redirect_uri=http://localhost:3000/auth&state=&grant_options[]=offline"
    )


def test_shopify_callback(client, mocker: MockerFixture, session: Session):
    mocker.patch(
        "app.deps.shopify.ShopifyClient.client.request",
        return_value=httpx.Response(
            request=httpx.Request("POST", "/api/auth/shopify_callback"),
            status_code=200,
            json={"access_token": "test_access_token"},
        ),
    )
    response = client.post(
        "/api/auth/shopify_callback", json={"shop": "test-shop", "code": "test-code"}
    )
    assert response.status_code == 200, response.json()
    assert response.json() == [
        {"customer_id": 1, "name": "test-shop.myshopify.com"}
    ], response.json()

    customers = session.exec(select(Customer)).all()
    assert len(customers) == 1
    customer = customers[0]
    assert len(customer.shops) == 1
    assert customer.shops[0].name == "test-shop.myshopify.com"
