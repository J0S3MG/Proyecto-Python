from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from Models.Venta import Venta

# --- Clase Base que valida los datos del Auto ---
class AutoBase(SQLModel): 
    """Modelo base para Auto"""
    marca: str = Field(max_length=100, description="Marca del auto")
    modelo: str = Field(max_length=100, description="Modelo del auto")  
    ano: int = Field(ge=1900,   le=datetime.now().year, description="Año de fabricación (entre 1900 y el año actual)")
    nro_chasis: str = Field(max_length=100, unique=True, description="Numero de chasis")

# --- Clase que mappea a la BD el Auto ---
class Auto(AutoBase, table=True): 
    """Modelo de la tabla Auto"""
    id: Optional[int] = Field(default=None, primary_key=True)
    # Relacion con ventas
    ventas: List["Venta"] = Relationship(back_populates="auto")

# --- DTO para crear un Auto ---
class AutoCreate(AutoBase):
    """Modelo para crear un Auto"""
    pass

# --- DTO para actualizar un Auto ---
class AutoUpdate(BaseModel):
    """Modelo para actualizar el Auto"""
    marca: Optional[str] = Field(max_length=100, description="Marca del auto")
    modelo: Optional[str] = Field(max_length=100, description="Modelo del auto")
    ano: Optional[int] = Field(ge=1900,   le=datetime.now().year, description="Año de fabricación (entre 1900 y el año actual)")
    nro_chasis: Optional[str] = Field(max_length=100, unique=True, description="Numero de chasis")
    
# --- DTO para la respuesta con la info del Auto ---
class AutoResponse(AutoBase):
    """Modelo para la respuesta de Auto"""
    id: int

# --- DTO para mostrar las ventas del auto ---
class AutoResponseWithVentas(AutoResponse):
    """Modelo para la respuesta del Auto con la informacion de la venta"""
    venta: Optional["VentaResponse"] = None

