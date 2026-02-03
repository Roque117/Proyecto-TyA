# Proyecto-TyA — Sistema de Control y Seguimiento de Rutinas Fitness

**Integrantes**
- Roque Josué Aguirre Viveros
- Luis Fernando Hernández Dimas
- Rafael Baltazar Bonifacio
- Erick Álvarez Balderas
- Jose Angel Nieves Franco
- Roberto Mauricio Maya Maldonado

## Propuesta 3: Sistema de Control y Seguimiento de Rutinas Fitness

**Descripción del proyecto**  
Aplicación web para gestionar rutinas de ejercicio, seguimiento de progreso físico, registro de peso y medidas corporales, y planes nutricionales básicos.

**Factibilidad**  
- Técnica: Alta — puede desarrollarse con tecnologías web estándar (FastAPI + base de datos relacional).  
- Económica: Alta — costos moderados y modelo de monetización con suscripciones.  
- Operativa: Alta — interfaz orientada a usuario con mínima capacitación.  
- Legal: Media-Alta — requiere avisos de responsabilidad y manejo de datos personales.

## Estructura del proyecto (scaffold)
- `main.py` — arranque y configuración de FastAPI.  
- `app/__init__.py` — paquete principal.  
- `app/routers/rutinas.py` — rutas para rutinas, progreso y registros.  
- `app/routers/__init__.py` — convierte `routers` en paquete.  
- `requirements.txt`, `.gitignore`, `README.md`

## Cómo ejecutar (desarrollo)
1. Crear y activar un entorno virtual.  
2. `pip install -r requirements.txt`  
3. `uvicorn main:app --reload`

## Notas
Este scaffold usa almacenamiento en memoria para demostración. Para producción, conectar una base de datos (Postgres/MySQL/SQLite) y añadir autenticación/privacidad.
