from fastapi import APIRouter, Depends
from app.models.customer import Customer
from app.deps.customer import get_current_customer

customer_router = APIRouter()


@customer_router.get("/me", response_model=Customer)
async def current_customer(current_customer: Customer = Depends(get_current_customer)):
    return current_customer
