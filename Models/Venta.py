from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel

# --- Clase Base que valida los datos de la Venta ---
class VentaBase(SQLModel):
    """Modelo base para Venta"""
    nombre_comprador: str = Field(max_length=200, description="Nombre completo del comprador")
    precio: float = Field(gt=0, description="Precio de venta del vehículo (debe ser mayor que 0)")
    fecha_venta: datetime = Field(default_factory=datetime.now, description="Fecha y hora de la venta")
    auto_id: int = Field(foreign_key="auto.id", description="Referencia al auto vendido (clave foránea)")

# --- Clase que mapea a la BD la Venta ---
class Venta(VentaBase, table=True):
    """Modelo de la tabla Venta"""
    id: Optional[int] = Field(default=None, primary_key=True)
    # Relación con Auto
    auto: Optional["Auto"] = Relationship(back_populates="ventas")

# --- DTO para crear una Venta ---
class VentaCreate(VentaBase):
    """Modelo para crear una Venta"""
    pass

# --- DTO para actualizar una Venta ---
class VentaUpdate(BaseModel):
    """Modelo para actualizar la Venta"""
    nombre_comprador: Optional[str] = Field(max_length=200, description="Nombre completo del comprador")
    precio: Optional[float] = Field(gt=0, description="Precio de venta del vehículo (debe ser mayor que 0)")
    fecha_venta: Optional[datetime] = Field(description="Fecha y hora de la venta")
    auto_id: Optional[int] = Field(description="Referencia al auto vendido (clave foránea)")

# --- DTO para la respuesta con la info de la Venta ---
class VentaResponse(VentaBase):
    """Modelo para la respuesta de Venta"""
    id: int

# --- DTO para mostrar la venta con información del auto ---
class VentaResponseWithAuto(VentaResponse):
    """Modelo para la respuesta de la Venta con la información del auto"""
    auto: Optional["AutoResponse"] = None