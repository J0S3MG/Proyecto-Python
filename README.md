# API con FastApi — José Manuel González

Una API REST que cumple con los principios SOLID. Que permite Crear y Gestionar autos y ventas.

### Estructura del Proyecto

```
PyServer/
├── main.py              # Aplicación FastAPI principal
├── database.py          # Configuración de base de datos PostgreSQL
├── deps.py              # "Factory" donde se hace la DIP.
├── Controllers.py       # Carpeta con los Controladores de la API (Auto, Venta)
├── Services.py          # Carpeta con los Servicios (Auto, Venta, Join)
|      └── Interfaces    # Carpeta con las Interfaces para los Servicios y Repositorios
├── Repositories.py      # Carpeta con los Repositorios (Auto, Venta)
├── Models.py            # Carpeta con los Modelos (Auto, Venta, Join)
└── requirements.txt     # Dependencias del proyecto

```

## Tecnologias Utilizadas

| Tecnología              | Descripción                                                                                                              |
| :---------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| **Python 3.13.7**       | Lenguaje principal del proyecto, usado para construir la lógica backend y manejar datos de forma eficiente.              |
| **FastAPI**             | Framework moderno y rápido para crear APIs con Python, basado en tipado y compatible con OpenAPI/Swagger.                |
| **Uvicorn [standard]**  | Servidor ASGI de alto rendimiento utilizado para ejecutar aplicaciones FastAPI.                                          |
| **SQLModel**            | ORM (Object Relational Mapper) que combina la simplicidad de SQLAlchemy y Pydantic para trabajar con bases de datos.     |
| **psycopg2-binary**     | Adaptador que permite la conexión y ejecución de consultas en bases de datos PostgreSQL.                                 |
| **Pydantic**            | Biblioteca para validación y manejo de datos usando modelos basados en anotaciones de tipo.                              |
| **pydantic-settings**   | Extensión de Pydantic para gestionar configuraciones del entorno (variables `.env`, configuraciones del servidor, etc.). |
| **python-dotenv**       | Permite cargar variables de entorno desde un archivo `.env`, facilitando la configuración y seguridad de credenciales.   |


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

### Endpoints de API

## Endpoints de Autos (/autos)

- POST /autos - Crear nuevo auto
- GET /autos - Listar autos con paginación
- GET /autos/{auto_id} - Obtener auto por ID
- PUT /autos/{auto_id} - Actualizar auto
- DELETE /autos/{auto_id} - Eliminar auto
- GET /autos/chasis/{numero_chasis}
- Buscar por número de chasis
- GET /autos/{auto_id}/with-ventas - Auto con sus ventas

## Endpoints de Ventas (/ventas)

- POST /ventas - Crear nueva venta
- GET /ventas - Listar ventas con paginación
- GET /ventas/{venta_id} - Obtener venta por ID
- PUT /ventas/{venta_id} - Actualizar venta
- DELETE /ventas/{venta_id} - Eliminar venta
- GET /ventas/auto/{auto_id} - Ventas de un auto específico
- GET /ventas/comprador/{nombre} - Ventas por nombre de comprador
- GET /ventas/{venta_id}/with-auto - Venta con información del auto

