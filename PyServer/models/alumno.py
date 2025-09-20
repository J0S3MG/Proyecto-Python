from pydantic import BaseModel # Validad que los datos sean los correctos.

# En este archivo creamos la clase alumno.
class Alumno(BaseModel):
    id: int
    name: str
    legajo: int
    nota: float

