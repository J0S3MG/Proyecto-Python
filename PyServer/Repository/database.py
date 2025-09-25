from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Aca hacemos la conexion a la base de datos.

# URL de conexión: postgres://usuario:password@host:puerto/nombre_db.
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/PruebaPy"

# Motor de conexión
engine = create_engine(DATABASE_URL)

# Sesión (para abrir/cerrar conexiones)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para los modelos de BD
Base = declarative_base()