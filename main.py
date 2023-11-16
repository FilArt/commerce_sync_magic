from fastapi import FastAPI
from fastapi.requests import Request
# from app.api import shopify, depop

from fastapi.templating import Jinja2Templates

app = FastAPI()

# app.include_router(shopify.router, prefix="/shopify", tags=["Shopify"])
# app.include_router(depop.router, prefix="/depop", tags=["Depop"])

templates = Jinja2Templates(directory="templates")

# Создание маршрута, который рендерит HTML-шаблон index.html
@app.get("/")
def read_home(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})

# Создание маршрута, который рендерит HTML-шаблон dashboard.html
@app.get("/dashboard")
def read_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {'request': request})


@app.get('/settings')
def read_settings(request: Request):
    return templates.TemplateResponse('settings.html', {'request': request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
