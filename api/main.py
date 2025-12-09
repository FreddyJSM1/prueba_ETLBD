from fastapi import FastAPI
from .routes import router

app = FastAPI(title="API Ventas")
app.include_router(router)