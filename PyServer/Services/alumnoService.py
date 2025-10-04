from typing import List, Optional # El Optional es para poder decir que es lo que devuelve un metodo.
from sqlalchemy.orm import Session # Esto nos permitira iniciar la sesion con la BD.
from Models.alumno import Alumno  # Traemos al obj Alumno.
from Repository.alumnoRepository import AlumnoRepository

# En este archivo definimos la clase que se encargara de la logica del negocio (CRUD).
class AlumnoService:
    def iniciar_sesion(self, db: Session): # Ahora en vez de inicializar una lista le pasamos una sesion.
        self.db = db

    # Obtener todos los alumnos
    def get_alumno_all(self) -> List[Alumno]:
        alu_db = AlumnoRepository(self.db)
        return alu_db.get_alumno_all() 

    # Obtener alumno por legajo
    def get_by_legajo(self, legajo: int) -> Optional[Alumno]: # Le decimos que devuelve un Alumno o None.
        alu_db = AlumnoRepository(self.db)
        return alu_db.get_by_legajo(legajo)

    # Crear alumno
    def create_alumno(self, alu: Alumno) -> Alumno:
        alu_db = AlumnoRepository(self.db)
        return alu_db.create_alumno(alu)

    # Actualizar alumno: El proceso es parecido al del Create solo que aca buscamos al alumno primero.
    def update_alumno(self, alu_upd: Alumno, alu_id: int) -> Optional[Alumno]:
        alu_db = AlumnoRepository(self.db)
        return alu_db.update_alumno(alu_upd,alu_id)

    # Eliminar alumno
    def delete_alumno(self, legajo: int) -> Optional[dict]: # En este caso devolvemos un msj.
        alu_db = AlumnoRepository(self.db)
        return alu_db.delete_alumno(legajo)

