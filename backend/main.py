from fastapi import FastAPI
from app.api.customer import customer_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import auth_router

app = FastAPI()

# routers
app.include_router(customer_router, prefix="/api/customer", tags=["Customer"])
app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])

# cors
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(shopify.router, prefix="/shopify", tags=["Shopify"])
# app.include_router(depop.router, prefix="/depop", tags=["Depop"])
