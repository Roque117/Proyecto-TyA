from fastapi import FastAPI
from app.routers.rutinas import router as rutinas_router

app = FastAPI(title="Proyecto-TyA - Rutinas Fitness", version="0.1.0")

app.include_router(rutinas_router, prefix="/api")

@app.get("/health", tags=["health"])
async def health():
    return {"status": "ok", "project": "Proyecto-TyA - Rutinas Fitness"}
