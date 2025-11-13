from datetime import datetime
from sqlmodel import Session, select
from typing import List, Optional
from Services.Interfaces.VentaInterface import VentaRepositoryInterface  
from Models.Venta import Venta, VentaCreate, VentaUpdate, VentaResponse

# -------------------- Implementación en Memoria del Repositorio --------------------
class VentaRepository(VentaRepositoryInterface):
    """Implementación de la VentaRepositoryInterface"""

    def __init__(self, session: Session):# Modificamos el constructor para que reciba una sesion de la BD.
        self.session = session 

    # -------------------------------------- CREATE ------------------------------------
    def create(self, nuevo: VentaCreate) -> VentaResponse:
        """Crea una nueva venta y la almacena"""
        nuevaVenta = Venta.model_validate(nuevo)# Validamos el obj nuevo con la clase Venta.
        self.session.add(nuevaVenta)# Marca el objeto nuevaVenta como pendiente de inserción en la base de datos.
        self.session.commit()# Envía la operacion pendiente (en este caso INSERT) a la base de datos.
        self.session.refresh(nuevaVenta)# Actualizá el objeto en memoria para que refleje el estado real de la base de datos.
        return nuevaVenta # Devolvemos la nueva venta. 
    # ----------------------------------------------------------------------------------


    # -------------------------------------- GET ALL -----------------------------------
    def get_all(self, skip: int = 0, limit: int = 100) -> List[VentaResponse]:
        """Devuelve una lista paginada de ventas"""
        query = select(Venta).offset(skip).limit(limit)# Construyo una consulta que selecciona todas las ventas, salta con skip y devuelve hasta limit.
        ventas = self.session.exec(query).all()# Ejecutá la consulta y transforma todas las filas como objetos del modelo Venta.
        return ventas # Devuelvo la lista con paginacion.
    # ----------------------------------------------------------------------------------


    # -------------------------------------- GET BY ID ---------------------------------
    def get_by_id(self, venta_id: int) -> Optional[VentaResponse]:
        """Devuelve una venta por su ID"""
        venta = self.session.get(Venta, venta_id)# Buscamos y devolvemos una venta especifica.
        return venta
    # ----------------------------------------------------------------------------------


    # ---------------------------------- GET BY AUTO ID --------------------------------
    def get_by_auto_id(self, auto_id: int) -> List[VentaResponse]:
        """Devuelve todas las ventas asociadas a un auto específico"""
        query = select(Venta).where(Venta.auto_id == auto_id)# Construyo una consulta que selecciona toda las ventas que coincidan con el auto_id.
        ventas = self.session.exec(query).all()# Ejecuto la consulta.
        return ventas # Devolvemos la lista.
    # ----------------------------------------------------------------------------------


    # -------------------------------- GET BY COMPRADOR --------------------------------
    def get_by_comprador(self, nombre: str) -> List[VentaResponse]:
        """Devuelve todas las ventas realizadas a un comprador específico"""
        nombre_lower = nombre.strip().lower()# Quitamos espacios en blancos y pasamos todo a minuscula.
        query = select(Venta).where(Venta.nom_comprador.ilike(nombre_lower))# Construimos la consulta SQL.
        resultados = self.session.exec(query).all()# Ejecutamos la consulta.
        return resultados # Devolvemos los resultados.
    # ----------------------------------------------------------------------------------


    # -------------------------------------- UPDATE ------------------------------------
    def update(self, venta_id: int, venta_update: VentaUpdate) -> Optional[VentaResponse]:
        """Actualiza los datos de una venta existente"""
        venta = self.get_by_id(venta_id)# Buscamos la venta en la base de datos.
        if not venta:
            return None
        # Obtenemos solo los campos que vienen en la request (no los que están vacíos).
        update_data = venta_update.model_dump(exclude_unset=True)

        for key, value in update_data.items():# Asignamos los nuevos valores a la instancia existente.
            setattr(venta, key, value)
        # Guardamos los cambios en la BD.
        self.session.add(venta)
        self.session.commit()
        self.session.refresh(venta)# Refrescamos la instancia para traer datos actualizados desde la BD.
        return venta # Devolvemos la venta modificada.
    # ----------------------------------------------------------------------------------


    # -------------------------------------- DELETE ------------------------------------
    def delete(self, venta_id: int) -> bool:
        """Elimina una venta por su ID"""
        venta = self.get_by_id(venta_id)# Buscar la venta en la base de datos.
        if not venta:
            return False
        self.session.delete(venta)# Eliminarla de la sesión.
        self.session.commit()# Confirmar los cambios (DELETE en la BD).
        return True
    # ----------------------------------------------------------------------------------    