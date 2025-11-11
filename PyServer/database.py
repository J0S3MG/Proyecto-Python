from sqlmodel import create_engine, Session, SQLModel
from typing import Generator

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/PruebaPy" # Le paso la url de la BD.

engine = create_engine(DATABASE_URL, echo=True) # Creamos el motor de la BD.

def create_db_and_tables():
    """Nos aseguramos de crear la BD y sus Tablas"""
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    """Devuelve una sesion de la BD"""
    with Session(engine) as session:
        yield session
