from fastapi import FastAPI, HTTPException # Traemos las clases de la carpeta lib.
from Services.alumnoService import AlumnoService # Traemos al Servicio.
from Models.alumno import Alumno # Traemos al Alumno.
from typing import List # Aca traemos el obj Lista.
#.\venv\Scripts\activate 

# Este Archivo es el Controlador.
app = FastAPI() # Aca creamos la variable que se va a encargar del servidor.

servicio = AlumnoService() # Creamos el servico.

# Los @app definen los endpoints de cada metodo.

# GET: Lista todos los alumnos.
@app.get("/alumno/", response_model=List[Alumno])
def get_all():
    return servicio.get_alumno_all()

# GET: Obtiene el alumno por legajo.
@app.get("/alumno/{legajo}", response_model=Alumno)
def get_by_legajo(legajo: int):
    alu = servicio.get_by_legajo(legajo)
    if alu:
        return alu
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

# POST: Crea al alumno.
@app.post("/alumno/", response_model=Alumno)
def create_alumno(alu: Alumno):
    a = servicio.create_alumno(alu)
    if a:
        return a
    raise HTTPException(status_code=400, detail="El Alumno no se pudo crear correctamente")

# PUT: Actualizamos el alumno.
@app.put("/alumno/{alu_id}", response_model=Alumno)
def update_alumno(alu_id: int, alu_upd: Alumno):
    alu = servicio.update_alumno(alu_upd, alu_id)
    if alu:
        return alu
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

# DELETE: Borramos el alumno.
@app.delete("/alumno/{legajo}")
def delete_alumno(legajo: int):
    msj = servicio.delete_alumno(legajo)
    if msj:
        return msj
    raise HTTPException(status_code=404, detail="Alumno no encontrado")