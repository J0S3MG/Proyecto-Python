from sqlalchemy import Column, Integer, String, Float # Con esto definimos cada columna de la tabla.
from Repository.database import Base # Esto nos ayuda a definir el ORM.

# En este archivo hacemos la Persistencia del Alumno.
class AlumnoDB(Base): # Es una clase ORM que representa la tabla alumno.
    __tablename__ = "alumno" # Nombre de la tabla en la base de datos.
    # Son los Atributo de la tabla.
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    legajo = Column(Integer, unique=True, nullable=False)
    nota = Column(Float, nullable=False)
