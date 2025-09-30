# Proyecto-Python
Como conectar la api a PostgesSQL (Persistencia):

1. Entramos en la VM (.\venv\Scripts\activate) y ejecutamos el comando: pip install sqlalchemy psycopg2-binary.
2. Lo que acabamos de instalar en la VM nos permitira hacer ORMs (SQLAlchemy) y conectarnos a la base de datos (psycopg2-binary).
3. Una vez instalado debemos crear en nuestro proyecto un archivo nombre.py aqui haremos la conexion a la base de datos. Fijarese en la carpeta Repository para mas info.
4. Ahora una vez hecho el paso anterior podemos crear una clase para utilizar como ORM (En mi caso alumnoDB).
5. Asi que una vez hecha la instalcion y acomodado el codigo para trabajar con PostrgresSQL queda pobrar y depurar.

Tips y Notas:
La manera en que funcionan la sesiones es muy parecido al manejo de archivos donde cada vez que abrimos una sesion debemos cerrarla. Tambien sepan que la linea 22 "Base.metadata.create_all(bind=engine)" en el archivo database.py a mi no me anduvo por ende tube que crear la tabla manualmente, mas haya de eso la forma de trabajar con la base se puede hacer medio trambolico pero nada que no se nos haga familiar.

Tecnologias a usar:

FastApi: FastAPI proporciona la estructura y las herramientas fundamentales para construir el núcleo de una API de manera muy eficiente. Las funcionalidades que nos brindan son:

 - Creación de Endpoints: Proporciona un sistema de enrutamiento intuitivo y potente para definir las rutas de tu API (por ejemplo, /usuarios, /alumno) y los metodos HTTP correspondientes (CRUD).

 - Validación y Serialización de Datos: Gracias a su integración con Pydantic, FastAPI gestiona automáticamente la validación de los datos de entrada, asegurando que cumplan con los tipos y formatos definidos. También se encarga de la serialización de los datos de salida a formato JSON.
 
 - Documentación Interactiva Automática: Obtienes una interfaz de usuario (Swagger UI y ReDoc) que permite explorar y probar los endpoints de tu API directamente desde el navegador solo poniendo localhost:8000/docs.

 - Alto Rendimiento: Construido sobre Starlette y Pydantic, FastAPI es uno de los frameworks de Python más rápidos disponibles. Su soporte para operaciones asíncronas (async/await) lo hace ideal para aplicaciones que necesitan manejar una gran cantidad de solicitudes concurrentes de manera eficiente.

 - Sistema de Inyección de Dependencias: Facilita la gestión de dependencias y la creación de código más modular, reutilizable y fácil de probar.

 - Seguridad Integrada: Ofrece herramientas para implementar esquemas de seguridad comunes, como OAuth2 con tokens JWT, de una manera sencilla.

Uvicorn: Uvicorn es un servidor web. Su trabajo principal es tomar el código de una aplicación web de Python (como una API hecha con FastAPI) y hacerlo accesible a través de internet o una red. Imagina que construyes una casa (la aplicación). Pues, Uvicorn es la puerta de entrada, la dirección y la infraestructura que permite a los visitantes (usuarios y otros servicios) llegar e interactuar con ella. En conjunto con otras tecnologias nos ayuda a desplegar (Deployment) nuestra aplicacion.

SQLAlchemy: Su función principal es la de un ORM (Object-Relational Mapper), lo que significa que "mapea" o convierte los objetos de código Python a tablas de la base de datos, y viceversa. Internamente SQLAlchemy traduce consultas en SQL real para el motor de base de datos que uses. Los veneficios de usar SQLAlchemy son:

- No hacer SQL Injections: En lugar de escribir sentencias SQL (como INSERT, UPDATE, SELECT), puedes manipular objetos de Python, y SQLAlchemy se encarga de generar el SQL correspondiente. Esto hace que tu código sea más legible, más fácil de mantener y menos propenso a errores de SQL.

- Independencia de la base de datos: SQLAlchemy puede trabajar con diferentes sistemas de bases de datos (PostgreSQL, MySQL, SQLite, etc.) con mínimos cambios en tu código. Simplemente cambias la "cadena de conexión" y SQLAlchemy se adapta.

- Abstracción y seguridad: Proporciona una capa de abstracción que te protege de algunas complejidades de las bases de datos y ayuda a prevenir ataques de inyección de SQL.

Psycopg2-Binary: Psycopg2 es un adaptador de base de datos para PostgreSQL en Python. Es el "intérprete" que traduce las instrucciones de Python  en comandos que el servidor de PostgreSQL puede entender. La variante -binary incluye todo compilado y listo para instalar, así no tenés que compilar librerías en tu máquina (más cómodo para desarrollo). Alguno de sus veneficios son:

- Conexión con PostgreSQL: Permite a los programas Python conectarse a bases de datos PostgreSQL.

- SQL Injection: Facilita la ejecución de comandos SQL para crear, modificar, eliminar y consultar datos en las tablas de la base de datos.

- Gestión de transacciones: Ayuda a manejar transacciones, asegurando la integridad de los datos (commit).

- Sincronización de datos: Es útil para desarrollar aplicaciones que requieren sincronización de datos en tiempo real entre Python y PostgreSQL.

- Facilidad de instalación: Su principal ventaja es la facilidad de instalación, ya que evita tener que instalar y configurar dependencias de compilación complejas, lo cual es necesario para instalar psycopg2 directamente desde el código fuente.  









