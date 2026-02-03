from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

router = APIRouter(tags=["rutinas"])

# --- Modelos ---
class Rutina(BaseModel):
    id: int
    nombre: str = Field(..., example="Full Body Principiantes")
    descripcion: Optional[str] = Field(None, example="Rutina para empezar en el gimnasio")
    ejercicios: List[str] = Field(default_factory=list)

class CrearRutina(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    ejercicios: List[str] = Field(default_factory=list)

class RegistroProgreso(BaseModel):
    usuario_id: int
    fecha: date
    peso_kg: Optional[float] = None
    medidas: Optional[dict] = None
    notas: Optional[str] = None

# --- Almacenamiento en memoria (demo) ---
_rutinas = [
    {"id": 1, "nombre": "Full Body Principiantes", "descripcion": "Rutina 3 días por semana", "ejercicios": ["sentadillas", "press banca", "remo"]},
    {"id": 2, "nombre": "Cardio y Resistencia", "descripcion": "Rutina enfocada en cardio", "ejercicios": ["carrera", "ciclismo", "saltos"]},
]
_progresos = []

# --- Endpoints ---
@router.get("/rutinas", response_model=List[Rutina])
async def listar_rutinas():
    return _rutinas

@router.get("/rutinas/{rutina_id}", response_model=Rutina)
async def obtener_rutina(rutina_id: int):
    for r in _rutinas:
        if r["id"] == rutina_id:
            return r
    raise HTTPException(status_code=404, detail="Rutina no encontrada")

@router.post("/rutinas", response_model=Rutina, status_code=201)
async def crear_rutina(payload: CrearRutina):
    nuevo_id = max([r["id"] for r in _rutinas], default=0) + 1
    nueva = {"id": nuevo_id, "nombre": payload.nombre, "descripcion": payload.descripcion, "ejercicios": payload.ejercicios}
    _rutinas.append(nueva)
    return nueva

@router.get("/progreso/{usuario_id}", response_model=List[RegistroProgreso])
async def obtener_progreso(usuario_id: int):
    return [p for p in _progresos if p["usuario_id"] == usuario_id]

@router.post("/registro", status_code=201)
async def registrar_progreso(payload: RegistroProgreso):
    _progresos.append(payload.dict())
    return {"ok": True, "registro": payload}
