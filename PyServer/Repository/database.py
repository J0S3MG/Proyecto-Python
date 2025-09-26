from sqlalchemy.ext.declarative import declarative_base # Sirve para definir la clase base de los modelos (tablas).
from sqlalchemy import create_engine # Crea el motor de conexión con la base de datos.
from sqlalchemy.orm import sessionmaker # Genera una fábrica de sesiones para conectarse a la base de datos.

# Aca hacemos la conexion a la base de datos.

# URL de conexión: MotorBD://Usuario:Password@Host:Puerto/Nombre_db.
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/PruebaPy"

# Motor de conexión: Es el objeto central que sabe cómo conectarse y hablar con PostgreSQL.
engine = create_engine(DATABASE_URL) # SQLAlchemy usa este motor para generar conexiones cuando hacen falta.

# Sesión: Devuelve una clase sesión personalizada. Es parecido a cuando trabajamos con archivos solo que aca abrimos y cerramos sesiones.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # sesiones para ejecutar queries.
# autocommit=False: no confirma cambios automáticamente.
# autoflush=False: no envía cambios automáticamente a la base hasta que hagas commit().

# Clase base/Padre para los Repositoriy que tengamos.
Base = declarative_base() 

# Crea las tablas en la base de datos  si no existen.
Base.metadata.create_all(bind=engine)

