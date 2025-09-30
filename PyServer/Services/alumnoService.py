from typing import List, Optional # El Optional es para poder decir que es lo que devuelve un metodo.
from sqlalchemy.orm import Session # Esto nos permitira iniciar la sesion con la BD.
from Models.alumno import Alumno  # Traemos al obj Alumno.
from Repository.alumnoDB import AlumnoDB  # Traemos nuestro ORM.

# En este archivo definimos la clase que se encargara de la logica del negocio (CRUD).
class AlumnoService:
    def iniciar_sesion(self, db: Session): # Ahora en vez de inicializar una lista le pasamos una sesion.
        self.db = db

    # Obtener todos los alumnos
    def get_alumno_all(self) -> List[Alumno]:
        alumnos_db = self.db.query(AlumnoDB).all() # Aca hacemos la consulta a la tabla en la BD (SELECT * FROM Alumno).
        return [Alumno.from_orm(alu) for alu in alumnos_db] # Aca transformamos cada fila en un Obj Alumno.

    # Obtener alumno por legajo
    def get_by_legajo(self, legajo: int) -> Optional[Alumno]: # Le decimos que devuelve un Alumno o None.
        alu_db = self.db.query(AlumnoDB).filter(AlumnoDB.legajo == legajo).first() # Buscamos al alumno en la base de datos.
        return Alumno.from_orm(alu_db) if alu_db else None # Si lo encuentra lo devuelve sino devuelve None.

    # Crear alumno
    def create_alumno(self, alu: Alumno) -> Alumno:
        alu_db = AlumnoDB( # Construimos el obj AlumnoDB a partir de los datos de alu.
            nombre=alu.nombre,
            legajo=alu.legajo,
            nota=alu.nota
        )
        self.db.add(alu_db) # Marca ese objeto para ser insertado en la base de datos, aun no ejecuta el INSERT.
        self.db.commit() # Confirmamos los cambios y ejecuta el INSERT.
        self.db.refresh(alu_db)  # Refrescamos la fila (alu_db) para autogenerar el Id.
        return Alumno.from_orm(alu_db) # Reconvertimos el alu_db a un Alumno.

    # Actualizar alumno: El proceso es parecido al del Create solo que aca buscamos al alumno primero.
    def update_alumno(self, alu_upd: Alumno, alu_id: int) -> Optional[Alumno]:
        alu_db = self.db.query(AlumnoDB).filter(AlumnoDB.id == alu_id).first()
        if alu_db:
            alu_db.nombre = alu_upd.nombre
            alu_db.legajo = alu_upd.legajo
            alu_db.nota = alu_upd.nota
            self.db.commit()
            self.db.refresh(alu_db)
            return Alumno.from_orm(alu_db)
        return None

    # Eliminar alumno
    def delete_alumno(self, legajo: int) -> Optional[dict]: # En este caso devolvemos un msj.
        alu_db = self.db.query(AlumnoDB).filter(AlumnoDB.legajo == legajo).first() # Buscamos al Alumno.
        if alu_db: # Si lo encuentra lo borra y confirma la accion con commit().
            self.db.delete(alu_db)
            self.db.commit()
            return {"detalle": "Alumno borrado correctamente"}
        return None


