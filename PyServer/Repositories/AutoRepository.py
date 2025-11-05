from typing import List, Optional
from Services.Interfaces.AutoInterface import AutoRepositoryInterface # La traemos desde el Servicio.
from Models.Auto import Auto, AutoCreate, AutoUpdate, AutoResponse
from Models.Venta import Venta
from datetime import datetime

class AutoRepository(AutoRepositoryInterface):
    """Implementación del AutoRepositoryInterface"""

    def __init__(self):
        # Ventas iniciales
        venta1 = Venta(id=1, nom_comprador="Juan Pérez", precio=15000.00,
                       fecha_venta=datetime(2024, 5, 10, 14, 30), auto_id=1)

        venta2 = Venta(id=2, nom_comprador="María González", precio=12500.50,
                       fecha_venta=datetime(2024, 6, 22, 10, 15), auto_id=2)

        venta3 = Venta(id=3, nom_comprador="Carlos López", precio=18000.75,
                       fecha_venta=datetime(2024, 7, 5, 16, 45), auto_id=3)

        venta4 = Venta(id=4, nom_comprador="Ana Torres", precio=16000.00,
                       fecha_venta=datetime(2024, 8, 12, 11, 10), auto_id=1)

        venta5 = Venta(id=5, nom_comprador="Ricardo Díaz", precio=17050.90,
                       fecha_venta=datetime(2024, 9, 18, 17, 55), auto_id=2)

        self.lista_autos: List[Auto] = [
            Auto(id=1, marca="Toyota", modelo="Corolla", ano=2020, nro_chasis="AAA111",
                 ventas=[venta1, venta4]),  

            Auto(id=2, marca="Ford", modelo="Focus", ano=2018, nro_chasis="BBB222",
                 ventas=[venta2, venta5]),  

            Auto(id=3, marca="Honda", modelo="Civic", ano=2021, nro_chasis="CCC333",
                 ventas=[venta3])            
        ]

        self.pk_autogenerada = 4


    # -------------------------------------- CREATE ------------------------------------
    def create(self, nuevo: AutoCreate) -> AutoResponse:
        """Crea un nuevo auto y lo almacena"""
        new_auto = Auto(
            id=self.pk_autogenerada,
            marca=nuevo.marca,
            modelo=nuevo.modelo,
            ano=nuevo.ano,
            nro_chasis=nuevo.nro_chasis,
            ventas=[]
        )
        self.pk_autogenerada += 1
        self.lista_autos.append(new_auto)
        return new_auto
    # ----------------------------------------------------------------------------------


    # ------------------------------------ GET ALL ------------------------------------
    def get_all(self, skip: int = 0, limit: int = 100) -> List[AutoResponse]:
        """Devuelve una lista paginada de autos"""# Esta es la forma de paginar en memoria.
        return self.lista_autos[skip: skip + limit]
    # ----------------------------------------------------------------------------------


    # ------------------------------------ GET BY ID -----------------------------------
    def get_by_id(self, auto_id: int) -> Optional[AutoResponse]:
        """Busca un auto por su ID"""
        return next((a for a in self.lista_autos if a.id == auto_id), None)
    # ----------------------------------------------------------------------------------


    # ---------------------------------- GET BY CHASIS ---------------------------------
    def get_by_chasis(self, nro_chasis: str) -> Optional[AutoResponse]:
        """Busca un auto por su número de chasis"""
        return next((a for a in self.lista_autos if a.nro_chasis == nro_chasis), None)
    # ----------------------------------------------------------------------------------


    # -------------------------------------- UPDATE ------------------------------------
    def update(self, auto_id: int, data: AutoUpdate) -> Optional[AutoResponse]:
        """Actualiza un auto existente por número de chasis"""
        auto = self.get_by_chasis(auto_id)
        if not auto:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(auto, key, value)

        return auto
    # ----------------------------------------------------------------------------------


    # -------------------------------------- DELETE ------------------------------------
    def delete(self, auto_id: int) -> bool:
        """Elimina un auto por su ID"""
        auto = self.get_by_id(auto_id)
        if not auto:
            return False

        self.lista_autos.remove(auto)
        return True
    # ----------------------------------------------------------------------------------
    
