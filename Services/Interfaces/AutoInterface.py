from abc import ABC, abstractmethod
from typing import List, Optional
from Models.Auto import AutoCreate, AutoUpdate, AutoResponse

# -------------------- Interfaz del Repositorio --------------------
class AutoRepositoryInterface(ABC): 
    """Interfaz para definir las operaciones del repositorio de Auto"""
    
    @abstractmethod # Devolvemos la lista entera de autos.
    def get_all(self, skip: int = 0, limit: int = 100) -> List[AutoResponse]:
        pass

    @abstractmethod # Buscamos el auto por id (GET/id).
    def get_by_id(self, auto_id: int) -> Optional[AutoResponse]:
        pass
    
    @abstractmethod # Buscamos el auto por nro de chasis (GET/chasis).
    def get_by_chasis(self,nro_chasis: str) -> Optional[AutoResponse]:
        pass

    @abstractmethod # Creamos el auto (POST).
    def create(self, nuevo: AutoCreate) -> AutoResponse:
        pass

    @abstractmethod # Actualizamos el auto buscando por su nro de chasis (PUT).
    def update(self, nro_chasis: str, auto_update: AutoUpdate) -> Optional[AutoResponse]:
        pass
    
    @abstractmethod # Borramos el auto buscando por su id (PK autogenerada por la BD) (DELETE).
    def delete(self, auto_id: int) -> bool:
        pass


# -------------------- Interfaz del Servicio --------------------
class AutoServiceInterface(ABC):
    """Interfaz para definir las operaciones del servicio de Auto"""

    @abstractmethod
    def create_auto(self, nuevo: AutoCreate) -> AutoResponse:
        pass

    @abstractmethod
    def get_autos(self, skip: int, limit: int) -> List[AutoResponse]:
        pass

    @abstractmethod
    def get_auto_by_id(self, auto_id: int) -> AutoResponse:
        pass
    
    @abstractmethod 
    def get_auto_by_chasis(self,nro_chasis: str) -> Optional[AutoResponse]:
        pass

    @abstractmethod
    def update_auto(self, nro_chasis: str, auto_update: AutoUpdate) -> AutoResponse:
        pass

    @abstractmethod
    def delete_auto(self, auto_id: int) -> bool:
        pass