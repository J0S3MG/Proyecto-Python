from fastapi import FastAPI, HTTPException # Traemos las clases de la carpeta lib.
from typing import List # Aca traemos el obj Lista.
from models.alumno import Alumno # Traemos al Alumno.
#.\venv\Scripts\activate 

# Este Archivo es el Controlador.
app = FastAPI() # Aca creamos la variable que se va a encargar del servidor.

# Inicializamos una lista vacía e indicamos que contendrá obj Alumnos.
alumnosss: List[Alumno] = [] 

# --- CRUD: Los @app definen los endpoints de cada metodo.

# GET: Lista todos los alumnos.
@app.get("/alumno/", response_model=List[Alumno])
def get_alumnos():
    return alumnosss

# GET: Obtiene el alumno por legajo.
@app.get("/alumno/{alumno_leg}", response_model=Alumno)
def get_alumno(alumno_leg: int):
    for alu in alumnosss:
        if alu.legajo == alumno_leg:
            return alu
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

# POST: Crea al alumno.
@app.post("/alumno/", response_model=Alumno)
def create_alumno(alu: Alumno):
    alumnosss.append(alu)
    return alu

# PUT: Actualizamos el alumno.
@app.put("/alumno/{alumno_id}", response_model=Alumno)
def update_alumno(alumno_id: int, updated_alu: Alumno):
    for i, alu in enumerate(alumnosss):
        if alu.id == alumno_id:
            alumnosss[i] = updated_alu
            return updated_alu
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

# DELETE: Borramos el alumno.
@app.delete("/alumno/{alu_leg}")
def delete_user(alu_leg: int):
    for i, alu in enumerate(alumnosss):
        if alu.legajo == alu_leg:
            del alumnosss[i]
            return {"detalle": "Alumno borrado correctamente"}
    raise HTTPException(status_code=404, detail="Alumno no encontrado")