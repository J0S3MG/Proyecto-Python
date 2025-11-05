from typing import List, Optional
from Models.Venta import VentaResponse
from Models.Auto import AutoResponse

# --- DTO para mostrar las ventas del auto ---
class AutoResponseWithVentas(AutoResponse):
    """Modelo para la respuesta del Auto con la informacion de las ventas"""
    ventas: List["VentaResponse"] = None

# --- DTO para mostrar la venta con información del auto ---
class VentaResponseWithAuto(VentaResponse):
    """Modelo para la respuesta de la Venta con la información del auto"""
    auto: Optional["AutoResponse"] = None
