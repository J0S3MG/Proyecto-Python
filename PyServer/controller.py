from fastapi import FastAPI, HTTPException, Depends # Depends: Las dependencias son funciones (como get_db) que FastAPI ejecuta automáticamente.
from Services.alumnoService import AlumnoService    # Y que inyecta los resultados en los endpoints.
from Repository.database import SessionLocal  # Esto nos ayuda a crear y cerrar sesiones (Como si fueran archivos). 
from Models.alumno import Alumno # Traemos al Alumno.
from sqlalchemy.orm import Session # Con esto podremos interacrtuar con la base de datos.
from typing import List # Aca traemos el obj Lista.
#.\venv\Scripts\activate 

# Este Archivo es el Controlador.
app = FastAPI() # Aca creamos la variable que se va a encargar del servidor.

# Dependencia para obtener una sesión de la base de datos en cada request.
def get_db(): # Crea y cierra sesiones automáticamente.
    db = SessionLocal() # Crea una nueva sesión (conexión a la BD).
    try:
        yield db # "devuelve" la sesión al endpoint que la necesite
    finally:
        db.close() # Cuando termina la request, la sesión se cierra.


# GET: Lista todos los alumnos.
@app.get("/alumno/", response_model=List[Alumno])
def get_all(db: Session = Depends(get_db)): # Depens: Inyectamos el resultado de get_db.
    servicio = AlumnoService(db) # Dejó de ser global porque cada request necesita su propia sesión aislada.
    return servicio.get_alumno_all() # Devolvemos la lista de alumnos.


# GET: Obtiene el alumno por legajo.
@app.get("/alumno/{legajo}", response_model=Alumno)
def get_by_legajo(legajo: int, db: Session = Depends(get_db)): # Iniciamos una nueva sesion.
    servicio = AlumnoService(db) # Le pasamos la sesion.
    alu = servicio.get_by_legajo(legajo) # Buscamos el alumno por legajo.
    if alu: # Devolvemos el alumno si lo encuentra.
        return alu
    raise HTTPException(status_code=404, detail="Alumno no encontrado")


# POST: Crea al alumno.
@app.post("/alumno/", response_model=Alumno)
def create_alumno(alu: Alumno, db: Session = Depends(get_db)):
    servicio = AlumnoService(db)
    a = servicio.create_alumno(alu)
    if a:
        return a
    raise HTTPException(status_code=400, detail="El Alumno no se pudo crear correctamente")


# PUT: Actualizamos el alumno.
@app.put("/alumno/{alu_id}", response_model=Alumno)
def update_alumno(alu_id: int, alu_upd: Alumno, db: Session = Depends(get_db)):
    servicio = AlumnoService(db)
    alu = servicio.update_alumno(alu_upd, alu_id)
    if alu:
        return alu
    raise HTTPException(status_code=404, detail="Alumno no encontrado")


# DELETE: Borramos el alumno.
@app.delete("/alumno/{legajo}")
def delete_alumno(legajo: int, db: Session = Depends(get_db)):
    servicio = AlumnoService(db)
    msj = servicio.delete_alumno(legajo)
    if msj:
        return msj
    raise HTTPException(status_code=404, detail="Alumno no encontrado")