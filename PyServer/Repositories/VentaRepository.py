from datetime import datetime
from typing import List, Optional
from Services.Interfaces.VentaInterface import VentaRepositoryInterface  
from Models.Venta import Venta, VentaCreate, VentaUpdate, VentaResponse

# -------------------- Implementación en Memoria del Repositorio --------------------
class VentaRepository(VentaRepositoryInterface):
    """Implementación de la VentaRepositoryInterface"""

    def __init__(self):
        # Lista de ventas iniciales
        self.lista_ventas: List[Venta] = [
            Venta(id=1, nom_comprador="Juan Pérez", precio=15000.00, fecha_venta=datetime(2024, 5, 10, 14, 30), auto_id=1),
            Venta(id=2, nom_comprador="María González", precio=12500.50, fecha_venta=datetime(2024, 6, 22, 10, 15), auto_id=2),
            Venta(id=3, nom_comprador="Carlos López", precio=18000.75, fecha_venta=datetime(2024, 7, 5, 16, 45), auto_id=3),
            Venta(id=4, nom_comprador="Ana Torres", precio=16000.00, fecha_venta=datetime(2024, 8, 12, 11, 10), auto_id=1),
            Venta(id=5, nom_comprador="Ricardo Díaz", precio=17050.90, fecha_venta=datetime(2024, 9, 18, 17, 55), auto_id=2),
        ]
        self.pk_autogenerada = 6

    # -------------------------------------- CREATE ------------------------------------
    def create(self, nuevo: VentaCreate) -> VentaResponse:
        """Crea una nueva venta y la almacena"""
        new_venta = Venta(
            id=self.pk_autogenerada,
            nom_comprador=nuevo.nom_comprador,
            precio=nuevo.precio,
            fecha_venta=nuevo.fecha_venta or datetime.now(),
            auto_id=nuevo.auto_id
        )
        self.lista_ventas.append(new_venta)
        self.pk_autogenerada += 1
        return new_venta
    # ----------------------------------------------------------------------------------


    # -------------------------------------- GET ALL -----------------------------------
    def get_all(self, skip: int = 0, limit: int = 100) -> List[VentaResponse]:
        """Devuelve una lista paginada de ventas"""
        return self.lista_ventas[skip: skip + limit]
    # ----------------------------------------------------------------------------------


    # -------------------------------------- GET BY ID ---------------------------------
    def get_by_id(self, venta_id: int) -> Optional[VentaResponse]:
        """Devuelve una venta por su ID"""
        return next((v for v in self.lista_ventas if v.id == venta_id), None)
    # ----------------------------------------------------------------------------------


    # ---------------------------------- GET BY AUTO ID --------------------------------
    def get_by_auto_id(self, auto_id: int) -> List[VentaResponse]:
        """Devuelve todas las ventas asociadas a un auto específico"""
        return [v for v in self.lista_ventas if v.auto_id == auto_id]
    # ----------------------------------------------------------------------------------


    # -------------------------------- GET BY COMPRADOR --------------------------------
    def get_by_comprador(self, nombre: str) -> List[VentaResponse]:
        """Devuelve todas las ventas realizadas a un comprador específico"""
        nombre_lower = nombre.strip().lower()
        return [v for v in self.lista_ventas if v.nom_comprador.lower() == nombre_lower]
    # ----------------------------------------------------------------------------------


    # -------------------------------------- UPDATE ------------------------------------
    def update(self, venta_id: int, venta_update: VentaUpdate) -> Optional[VentaResponse]:
        """Actualiza los datos de una venta existente"""
        venta = self.get_by_id(venta_id)
        if not venta:
            return None

        update_data = venta_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(venta, key, value)

        return venta
    # ----------------------------------------------------------------------------------


    # -------------------------------------- DELETE ------------------------------------
    def delete(self, venta_id: int) -> bool:
        """Elimina una venta por su ID"""
        venta = self.get_by_id(venta_id)
        if not venta:
            return False

        self.lista_ventas.remove(venta)
        return True
    # ----------------------------------------------------------------------------------    