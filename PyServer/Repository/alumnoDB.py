from sqlalchemy import Column, Integer, String, Float
from database import Base

class AlumnoDB(Base):
    __tablename__ = "alumnos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    legajo = Column(Integer, unique=True, nullable=False)
    nota = Column(Float, nullable=False)
