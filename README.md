# API de Gestion de Autos y Ventas con FastAPI

Una API REST que cumple con los principios SOLID. Que permite Crear y Gestionar autos y ventas.

## Características

### Auto CRUD
- Obtener todos los autos paginados.
- Obtener un auto por ID o Chasis.
- Obtener un auto con sus ventas.
- Agregar nuevos autos o modificar existentes.
- Eliminar un auto. 

### Venta CRUD 
- Obtener todas las ventas paginadas.
- Obtener una venta por ID o Comprador o Auto.
- Obtener una venta con su auto.
- Agregar nuevas ventas o modificar existentes.
- Eliminar una venta.

## Tecnologias Utilizadas

- Python 3.13.7 – Lenguaje principal del proyecto, usado para construir la lógica backend y manejar datos de forma eficiente.
- FastAPI 0.115.0 – Framework moderno y rápido para crear APIs con Python, basado en tipado y compatible con OpenAPI/Swagger.
- Uvicorn [standard] 0.30.1 – Servidor ASGI de alto rendimiento utilizado para ejecutar aplicaciones FastAPI.
- SQLModel 0.0.22 – ORM (Object Relational Mapper) que combina la simplicidad de SQLAlchemy y Pydantic para trabajar con bases de datos.
- psycopg2-binary 2.9.11 – Adaptador que permite la conexión y ejecución de consultas en bases de datos PostgreSQL.
- Pydantic 2.9.2 – Biblioteca para validación y manejo de datos usando modelos basados en anotaciones de tipo.
- pydantic-settings 2.4.0 – Extensión de Pydantic para la configuración del entorno (variables .env, configuraciones del servidor, etc.).
- python-dotenv 1.0.1 – Permite cargar variables de entorno desde un archivo .env, facilitando la configuración y la seguridad de credenciales.

## Pasos para la Instalación y Configuración

1. **Clonar o descargar el proyecto**
   ```bash
   git clone https://github.com/J0S3MG/Proyecto-Python.git
   cd PyServer
   ```

2. **Crear un entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual**
   ```bash
   .\venv\Scripts\activate
   ```

4. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```



## Ejecutar la Aplicación

1. **Asegúrate de tener el entorno virtual activado**
   ```bash
   # En Windows
   .\venv\Scripts\activate
   ```

2. **Iniciar el servidor de desarrollo**
   ```bash
   uvicorn main:app --reload
   ```

3. **La aplicación estará disponible en:**
   - **API**: http://localhost:8000
   - **Documentación Interactiva**: http://localhost:8000/docs
   - **Documentación Alternativa**: http://localhost:8000/redoc

### Detener la Aplicación y Desactivar el Entorno

1. **Para detener el servidor:** Presiona `Ctrl + C` en la terminal

2. **Para desactivar el entorno virtual:**
   ```bash
   deactivate
   ```
