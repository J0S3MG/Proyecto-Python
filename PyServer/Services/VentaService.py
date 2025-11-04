from typing import List
from Services.Interfaces.VentaInterface import VentaRepositoryInterface, VentaServiceInterface
from Models.Venta import VentaCreate, VentaUpdate, VentaResponse


class VentaService(VentaServiceInterface):
    """Implementación del VentaServiceInterface"""

    def __init__(self, repo: VentaRepositoryInterface):
        self.repo = repo  # Inyección de dependencia del repositorio


    # ------------------------------------ CREATE ------------------------------------
    def create_venta(self, nuevo: VentaCreate) -> VentaResponse:
        """Crea una nueva venta"""
        new_venta = self.repo.create(nuevo)
        return VentaResponse.model_validate(new_venta)
    # --------------------------------------------------------------------------------


    # ------------------------------------ GET ALL -----------------------------------
    def get_ventas(self, skip: int = 0, limit: int = 100) -> List[VentaResponse]:
        """Devuelve una lista paginada de todas las ventas"""
        ventas = self.repo.get_all(skip=skip, limit=limit)
        return [VentaResponse.model_validate(venta) for venta in ventas]
    # --------------------------------------------------------------------------------


	# ------------------------------------ GET BY ID ---------------------------------
    def get_venta_by_id(self, auto_id: int) -> VentaResponse:
        """Devuelve una venta por su ID"""
        venta = self.repo.get_by_id(auto_id)
        if not venta:
            raise ValueError(f"Venta con id {auto_id} no encontrada")
        return VentaResponse.model_validate(venta)
    # --------------------------------------------------------------------------------


    # ----------------------------- GET VENTAS BY AUTO --------------------------------
    def get_ventas_by_auto(self, auto_id: int, skip: int = 0, limit: int = 100) -> List[VentaResponse]:
        """Devuelve todas las ventas relacionadas con un auto"""
        ventas = self.repo.get_ventas_by_auto(auto_id, skip=skip, limit=limit)
        return [VentaResponse.model_validate(venta) for venta in ventas]
    # --------------------------------------------------------------------------------


    # --------------------------- GET VENTAS BY COMPRADOR -----------------------------
    def get_ventas_by_comprador(self, nombre: str) -> List[VentaResponse]:
        """Devuelve todas las ventas realizadas a un comprador por su nombre"""
        ventas = self.repo.get_by_comprador(nombre)
        return [VentaResponse.model_validate(venta) for venta in ventas]
    # --------------------------------------------------------------------------------


    # ------------------------------------ UPDATE ------------------------------------
    def update_venta(self, venta_id: int, venta_update: VentaUpdate) -> VentaResponse:
        """Actualiza una venta por su ID"""
        venta_actualizada = self.repo.update(venta_id, venta_update)
        if not venta_actualizada:
            raise ValueError(f"No se pudo actualizar la venta con id {venta_id}")
        return VentaResponse.model_validate(venta_actualizada)
    # --------------------------------------------------------------------------------


    # ------------------------------------ DELETE ------------------------------------
    def delete_venta(self, venta_id: int) -> bool:
        """Elimina una venta por su ID"""
        eliminado = self.repo.delete(venta_id)
        if not eliminado:
            raise ValueError(f"No se pudo eliminar la venta con id {venta_id}")
        return True
    # --------------------------------------------------------------------------------