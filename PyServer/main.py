from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine
from Controllers.AutoController import router as auto_router # Importamos el enrutador y le ponemos un nuevo nombre.
from Controllers.VentaController import router as venta_router # Importamos el enrutador y le ponemos un nuevo nombre.

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("="*80)
    print("🚀 INICIANDO APLICACIÓN")
    print("="*80)
    create_db_and_tables()
    yield
    print("⛔ App terminando...")
    
app = FastAPI(
    title="FastAPI CRUD Ventas-Auto", 
    description="Trabajo Backend Prog IV 2025", 
    version="1.0.0",
    lifespan=lifespan
)

# Incluimos el router de auto.
app.include_router(auto_router)

# Incluimos el router de venta.
app.include_router(venta_router)