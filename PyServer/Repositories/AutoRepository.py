from typing import List, Optional
from sqlmodel import Session, select
from Services.Interfaces.AutoInterface import AutoRepositoryInterface # La traemos desde el Servicio.
from Models.Auto import Auto, AutoCreate, AutoUpdate, AutoResponse
from Models.Venta import Venta
from datetime import datetime

class AutoRepository(AutoRepositoryInterface):
    """Implementación del AutoRepositoryInterface"""

    def __init__(self,session: Session):
        self.session = session 


    # -------------------------------------- CREATE ------------------------------------
    def create(self, nuevo: AutoCreate) -> AutoResponse:
        """Crea un nuevo auto y lo almacena"""
        nuevoAuto = Auto.model_validate(nuevo)
        self.session.add(nuevoAuto)
        self.session.commit()
        self.session.refresh(nuevoAuto)
        return nuevoAuto
    # ----------------------------------------------------------------------------------


    # ------------------------------------ GET ALL ------------------------------------
    def get_all(self, skip: int = 0, limit: int = 100) -> List[AutoResponse]:
        """Devuelve una lista paginada de autos"""
        query = select(Auto).offset(skip).limit(limit)
        autos = self.session.exec(query).all()
        return autos
    # ----------------------------------------------------------------------------------


    # ------------------------------------ GET BY ID -----------------------------------
    def get_by_id(self, auto_id: int) -> Optional[AutoResponse]:
        """Busca un auto por su ID"""
        auto = self.session.get(Auto, auto_id)
        return auto
    # ----------------------------------------------------------------------------------


    # ---------------------------------- GET BY CHASIS ---------------------------------
    def get_by_chasis(self, nro_chasis: str) -> Optional[AutoResponse]:
        """Busca un auto por su número de chasis"""
        query = select(Auto).where(Auto.nro_chasis == nro_chasis)# Construyo la consulta.
        auto = self.session.exec(query).first()# Ejecutamos y devolvemos la primer coincidencia.
        return auto
    # ----------------------------------------------------------------------------------


    # -------------------------------------- UPDATE ------------------------------------
    def update(self, auto_id: int, auto_update: AutoUpdate) -> Optional[AutoResponse]:
        """Actualiza un auto existente"""
        auto = self.get_by_id(auto_id)# Buscamos el auto en la base de datos.
        if not auto:
            return None
        # Obtenemos solo los campos que vienen en la request (no los que están vacíos).
        update_data = auto_update.model_dump(exclude_unset=True)

        for key, value in update_data.items():# Asignamos los nuevos valores a la instancia existente.
            setattr(auto, key, value)
        # Guardamos los cambios en la BD.
        self.session.add(auto)
        self.session.commit()
        self.session.refresh(auto)# Refrescamos la instancia para traer datos actualizados desde la BD.
        return auto # Devolvemos la venta modificada.
    # ----------------------------------------------------------------------------------


    # -------------------------------------- DELETE ------------------------------------
    def delete(self, auto_id: int) -> bool:
        """Elimina un auto por su ID"""
        auto = self.get_by_id(auto_id)# Buscamos el auto en la base de datos.
        if not auto:
            return False
        self.session.delete(auto)# Eliminarla de la sesión.
        self.session.commit()# Confirmar los cambios (DELETE en la BD).
        return True
    # ----------------------------------------------------------------------------------
    
