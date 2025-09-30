from Models.alumno import Alumno
from typing import List # Aca traemos el obj Lista.

# En este archivo definimos la clase que se encargara de la logica del negocio (CRUD).
class AlumnoService:
    def __init__(self):
        self.alumnosss: List[Alumno] = []  # lista en memoria

    # Retornamos la lista con todos los alumnos.
    def get_alumno_all(self) -> List[Alumno]:
        return self.alumnosss
    
    # Retornamos el alumno segun el legajo.
    def get_by_legajo(self,legajo: int) -> Alumno | None: # Aca le digo lo que va a retornar. Esto tmb se puede hacer con la clase Optional.
        for alu in self.alumnosss:
            if alu.legajo == legajo:
                return alu # Retornamos el alumno.
        return None  # si no encontró ninguno retornamos none.

    # Creamos el alumno.
    def create_alumno(self,alu: Alumno) -> Alumno | None:
        if alu != None:
            self.alumnosss.append(alu)
            return alu
        return None 

    # Modificamos el alumno en base al id.
    def update_alumno(self,alu_upd: Alumno, alu_id: int) -> Alumno | None:
        for i, alu in enumerate(self.alumnosss):
            if alu.id == alu_id:
                self.alumnosss[i] = alu_upd
                return alu_upd # Retornamos el alumno actualizado.
        return None # Si no encontramos el alumno a modificar.

    # Borramos un alumno segun el legajo.
    def delete_alumno(self,legajo: int) -> dict | None:
        for i, alu in enumerate(self.alumnosss):
            if alu.legajo == legajo:
                del self.alumnosss[i]
                return {"detalle": "Alumno borrado correctamente"}
        return None # Si no encontro el alumno a borrar.


