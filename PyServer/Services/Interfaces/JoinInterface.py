from abc import ABC, abstractmethod
from typing import List, Optional
from Models.Join import AutoResponseWithVentas, VentaResponseWithAuto

class JoinServiceInterface(ABC):

    @abstractmethod
    def get_auto_with_ventas(self, auto_id: int) -> Optional[AutoResponseWithVentas]:
        """Obtiene un auto con todas sus ventas"""
        pass

    @abstractmethod
    def get_venta_with_auto(self, venta_id: int) -> Optional[VentaResponseWithAuto]:
        """Obtiene una venta con los datos del auto vendido"""
        pass