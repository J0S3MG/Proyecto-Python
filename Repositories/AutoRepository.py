from typing import List, Optional
from Services.Interfaces.AutoInterface import AutoRepositoryInterface # La traemos desde el Servicio.
from Models.Auto import Auto, AutoCreate, AutoUpdate, AutoResponse

class AutoRepository(AutoRepositoryInterface):
    """Implementación en memoria del AutoRepositoryInterface"""

    def __init__(self):
        self.lista_autos: List[Auto] = [
            Auto(id=1, marca="Toyota", modelo="Corolla", ano=2020, nro_chasis="AAA111", ventas=[]),
            Auto(id=2, marca="Ford", modelo="Focus", ano=2018, nro_chasis="BBB222", ventas=[]),
            Auto(id=3, marca="Honda", modelo="Civic", ano=2021, nro_chasis="CCC333", ventas=[]),
        ]
        self.pk_autogenerada = 4


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


    # -------------------------------------- UPDATE ------------------------------------
    def update(self, nro_chasis: str, data: AutoUpdate) -> Optional[AutoResponse]:
        """Actualiza un auto existente por número de chasis"""
        auto = self.get_by_chasis(nro_chasis)
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
    
