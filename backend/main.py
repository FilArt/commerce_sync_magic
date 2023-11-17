from fastapi import FastAPI
from fastapi.requests import Request
# from app.api import shopify, depop


app = FastAPI()

# app.include_router(shopify.router, prefix="/shopify", tags=["Shopify"])
# app.include_router(depop.router, prefix="/depop", tags=["Depop"])



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=9000, log_level="info")
