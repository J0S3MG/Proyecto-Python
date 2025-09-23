# Proyecto-Python
Como crear nuestro proyecto para trabajar con Python:

Descargar Python: https://www.python.org/
Lo que acabamos de descargar es el interprete de python 3.13.7, para verificar la instalacion en el powershell o cmd hacer: python --version. IMPORTANTE al Instalar tilde la opcion de path.
Una vez instalado debemos hacer el repo o buscar la carpeta donde guardar el proyecto. Si hacen el repo haganlo sin el .gitignore (Copiar el gitignore de mi proyecto).
Ahora una vez colocado dentro de la carpeta donde vamos a guardar el proyecto debemos crear una Maquina Virtual que nos pertimita levantar el servidor y trabajar con Python para esto ejecute el siguiente comando dentro de esa ubicacion: python -m venv venv . Esto creara una carpeta llamada venv que sera la VM donde correra el servidor.
Ahora una vez creada la carpeta venv debemos activar la VM para esto abrimos un powershell o cmd en la misma ubicacion que antes y ejecutamos este comando: .\venv\Scripts\activate, esto activara la VM una vez activada en el powershell o cmd veremos algo como esto "(venv) E:\Direccion donde abrimos el powershell o cmd>" eso significa que estamos en la Maquina Virtual.
Una vez ubicados en la VM debemos instalar las librerias a usar para eso escribimos el comando: pip install fastapi uvicorn . Este comando instalara por un lado el framework (Libreria) FastApi que nos brinda lo necesario para crear la API y Uvicorn sera el servidor donde correra nuestra API.
Ahora con todo esto instalado en la misma ubicacion de la carpeta venv creamos un archivo de tipo .py donde empezaremos a crear nuestra API.
Si llegaste hasta aqui felicidades tienes tu proyecto ya encaminado ve a VS Code y empieza a codear.
Para probar como funciona tu API ve a la VM (Punto 5) y ejecuta el siguiente comando: uvicorn nombreArchivo: instanciaDeLaClaseFastApi --reload y dale enter una vez el servidor este en linea vas a la direccion IP donde esta corriendo (normalmente el puerto 8000) y usa /docs para poder acceder al Swagger y testear los endpoints.
Tips y Notas:

Si vas a guiarte con mi proyecto te en cuenta que yo lo organice de manera diferente a como lo explico es decir clone mi repo y dentro cree otra carpeta y dentro de esa carpeta puse la VM e hice mi codigo. Ademas sepan que estan trabajando con python en si no tiene una estrucura como JAVA o C# donde por ejemplo cada archivo era una clase en si mismo sino que aca los archivos pueden contener lo que sea esto se los digo de cara a trabajar con la IA que les va a dar todo el codigo pegado como si fuera programacion imperativa esto es asi dado que Python es un lenguaje de interpretado no compilado como los anteriores mensionados. En fin aca debemos ser mas rigurosos a la hora de organizar todo xq no contamos con un IDE que nos advierta si lo hacemos mal. Otro detalle es que la VM que creamos crea una copia de la version de python que tengamos instalada muy diferente de lo que enseño el profe que las hace con cualquier version de python.

Tecnologias a usar:

FastApi: FastAPI proporciona la estructura y las herramientas fundamentales para construir el núcleo de una API de manera muy eficiente. Las funcionalidades que nos brindan son:

Creación de Endpoints: Proporciona un sistema de enrutamiento intuitivo y potente para definir las rutas de tu API (por ejemplo, /usuarios, /alumno) y los metodos HTTP correspondientes (CRUD).
Validación y Serialización de Datos: Gracias a su integración con Pydantic, FastAPI gestiona automáticamente la validación de los datos de entrada, asegurando que cumplan con los tipos y formatos definidos. También se encarga de la serialización de los datos de salida a formato JSON.
Documentación Interactiva Automática: Obtienes una interfaz de usuario (Swagger UI y ReDoc) que permite explorar y probar los endpoints de tu API directamente desde el navegador solo poniendo localhost:8000/docs.
Alto Rendimiento: Construido sobre Starlette y Pydantic, FastAPI es uno de los frameworks de Python más rápidos disponibles. Su soporte para operaciones asíncronas (async/await) lo hace ideal para aplicaciones que necesitan manejar una gran cantidad de solicitudes concurrentes de manera eficiente.
Sistema de Inyección de Dependencias: Facilita la gestión de dependencias y la creación de código más modular, reutilizable y fácil de probar.
Seguridad Integrada: Ofrece herramientas para implementar esquemas de seguridad comunes, como OAuth2 con tokens JWT, de una manera sencilla.
Uvicorn: Uvicorn es un servidor web. Su trabajo principal es tomar el código de una aplicación web de Python (como una API hecha con FastAPI) y hacerlo accesible a través de internet o una red. Imagina que construyes una casa (la aplicación). Pues, Uvicorn es la puerta de entrada, la dirección y la infraestructura que permite a los visitantes (usuarios y otros servicios) llegar e interactuar con ella. En conjunto con otras tecnologias nos ayuda a desplegar (Deployment) nuestra aplicacion.
