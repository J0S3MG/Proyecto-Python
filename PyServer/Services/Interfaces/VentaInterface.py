from abc import ABC, abstractmethod
from typing import List, Optional
from Models.Venta import VentaCreate, VentaUpdate, VentaResponse


# -------------------- Interfaz del Repositorio --------------------
class VentaRepositoryInterface(ABC):
    """Interfaz para definir las operaciones del repositorio de venta"""

    @abstractmethod  # Crear una venta (POST)
    def create(self, nuevo: VentaCreate) -> VentaResponse:
        """Crea una nueva venta"""
        pass

    @abstractmethod  # Obtener todas las ventas (GET)
    def get_all(self, skip: int = 0, limit: int = 100) -> List[VentaResponse]:
        """Devuelve una lista paginada de todas las ventas"""
        pass

    @abstractmethod  # Obtener una venta por su ID (GET /id)
    def get_by_id(self, venta_id: int) -> Optional[VentaResponse]:
        """Devuelve una venta por su ID"""
        pass

    @abstractmethod  # Obtener ventas por ID de auto (GET /auto/{auto_id})
    def get_by_auto_id(self, auto_id: int) -> List[VentaResponse]:
        """Devuelve todas las ventas asociadas a un auto específico"""
        pass

    @abstractmethod  # Obtener ventas por nombre del comprador (GET /comprador/{nombre})
    def get_by_comprador(self, nombre: str) -> List[VentaResponse]:
        """Devuelve todas las ventas realizadas a un comprador específico"""
        pass

    @abstractmethod  # Actualizar una venta (PUT)
    def update(self, venta_id: int, venta_update: VentaUpdate) -> Optional[VentaResponse]:
        """Actualiza los datos de una venta existente"""
        pass

    @abstractmethod  # Eliminar una venta (DELETE)
    def delete(self, venta_id: int) -> bool:
        """Elimina una venta por su ID"""
        pass


# -------------------- Interfaz del Servicio --------------------
class VentaServiceInterface(ABC):
    """Interfaz para definir las operaciones del servicio de venta"""

    @abstractmethod
    def create_venta(self, nuevo: VentaCreate) -> VentaResponse:
        pass

    @abstractmethod
    def get_ventas(self, skip: int = 0, limit: int = 100) -> List[VentaResponse]:
        pass
    
    @abstractmethod 
    def get_venta_by_id(self, auto_id: int) -> VentaResponse:
        pass
    
    @abstractmethod 
    def get_ventas_by_auto(self, auto_id: int) -> List[VentaResponse]:
        pass

    @abstractmethod
    def get_ventas_by_comprador(self, nombre: str) -> List[VentaResponse]:
        pass

    @abstractmethod
    def update_venta(self, venta_id: int, venta_update: VentaUpdate) -> VentaResponse:
        pass

    @abstractmethod
    def delete_venta(self, venta_id: int) -> bool:
        pass