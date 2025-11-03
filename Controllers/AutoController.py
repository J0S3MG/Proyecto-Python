from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from Models.Auto import AutoCreate, AutoUpdate, AutoResponse
from Services.Interfaces.AutoInterface import AutoServiceInterface # Aca traemos para hacer la Inyeccion de dependencia.
from deps import get_auto_service # Este metodo hace la Inyeccion de Dep. Recordemos que en FastApi lo hacemos a travez de funciones (metodos).

#Definimos la ruta para los endpoints de auto.
router = APIRouter(prefix="/autos", tags=["Autos"])

# -------------------------------- POST ---------------------------------------------
# Definimos el endpoint: POST/autos.
@router.post("/", response_model=AutoResponse, status_code=status.HTTP_201_CREATED)
def create_auto( nuevo: AutoCreate,
    servicio: AutoServiceInterface = Depends(get_auto_service)) -> AutoResponse:
    # ↑ Aquí hacemos la Inyeccion de Dependencia. ↑ deps nos trae este metodo.
    try:
        return servicio.create_auto(nuevo) # Agregamos el nuevo auto.
    except Exception as e: # Manejo de Excepciones.
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------

# ---------------------------------- GET ALL ----------------------------------------
# Definimos el endpoint: GET/autos.
@router.get("/", response_model=List[AutoResponse])
def get_autos( # Definimos los limites para devolver la lista paginada. 
    skip: int = Query(0, ge=0, description="Número de autos a saltar"),
    limit: int = Query(100, ge=1, le=1000, description="Número de autos a devolver"),
    service: AutoServiceInterface = Depends(get_auto_service) # DIP
) -> List[AutoResponse]:
    return service.get_autos(skip, limit) # Devolvemos la lista paginada.
# -----------------------------------------------------------------------------------

# -------------------------------- GET BY ID ----------------------------------------
# Definimos el endpoint: GET/autos/{auto_id}.
@router.get("/{auto_id}", response_model=AutoResponse)
def get_auto( auto_id: int, 
    service: AutoServiceInterface = Depends(get_auto_service) ) -> AutoResponse:
    try:
        return service.get_auto_by_id(auto_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------

# ------------------------------- GET BY CHASIS -------------------------------------
# Definimos el endpoint: GET/autos/{nro_chasis}.
@router.get("/chasis/{nro_chasis}", response_model=AutoResponse)
def get_auto_by_chasis( nro_chasis: str,
    service: AutoServiceInterface = Depends(get_auto_service)) -> AutoResponse:
    try:
        return service.get_auto_by_chasis(nro_chasis)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------

# -------------------------------- PUT ----------------------------------------------
# Definimos el endpoint: PUT/autos/{auto_id}.
@router.put("/{nro_chasis}", response_model=AutoResponse)
def update_auto( nro_chasis: str, data: AutoUpdate,
    service: AutoServiceInterface = Depends(get_auto_service)) -> AutoResponse:
    try:
        return service.update_auto(nro_chasis, data)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
# ----------------------------------------------------------------------------------

# ---------------------------------- DELETE ----------------------------------------
# Definimos el endpoint: DELETE/autos/{auto_id}.
@router.delete("/{auto_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_auto( auto_id: int,
    service: AutoServiceInterface = Depends(get_auto_service)) -> None:
    try:
        deleted = service.delete_auto(auto_id)
        if not deleted:
            raise Exception("No se pudo eliminar el auto")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
# ----------------------------------------------------------------------------------