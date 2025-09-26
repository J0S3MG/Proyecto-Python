from pydantic import BaseModel # Validad que los datos sean los correctos.

# En este archivo creamos la clase alumno (se usa para exponer datos seguros y validados). 
class Alumno(BaseModel): # Por defecto pydantic solo entiende obj Dict (Diccionarios).
    id: int
    nombre: str
    legajo: int
    nota: float
    # Con from_attributes pydantic ahora es capaz de entender (Validar) obj ORM.
    class Config:
        from_attributes = True

