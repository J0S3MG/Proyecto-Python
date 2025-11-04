from fastapi import FastAPI
from contextlib import asynccontextmanager
from Controllers.AutoController import router as auto_router # Importamos el enrutador y le ponemos un nuevo nombre.
from Controllers.VentaController import router as venta_router # Importamos el enrutador y le ponemos un nuevo nombre.

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App iniciando...")
    # Código de startup
    yield
    print("App terminando...")
    # Código de shutdown
    
app = FastAPI(
    title="FastAPI CRUD Prueba", 
    description="Trabajo Backend Prog IV 2025", 
    version="1.0.0",
    lifespan=lifespan
)

# Incluimos el router de auto.
app.include_router(auto_router)

# Incluimos el router de venta.
app.include_router(venta_router)