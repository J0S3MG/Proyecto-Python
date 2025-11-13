from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from Models.Join import AutoResponseWithVentas
from Models.Auto import AutoCreate, AutoUpdate, AutoResponse
from Services.Interfaces.AutoInterface import AutoServiceInterface # Aca traemos para hacer la Inyeccion de dependencia.
from Services.Interfaces.JoinInterface import JoinServiceInterface
from deps import get_auto_service, get_join_service # Este metodo hace la Inyeccion de Dep. Recordemos que en FastApi lo hacemos a travez de funciones (metodos).

#Definimos la ruta para los endpoints de auto.
router = APIRouter(prefix="/autos", tags=["Autos"])

# -------------------------------- POST ---------------------------------------------
# Definimos el endpoint: POST/autos.
@router.post("/", response_model=AutoResponse, status_code=status.HTTP_201_CREATED, summary="Crea un Auto", operation_id="Crear_Auto")
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
@router.get("/", response_model=List[AutoResponse], summary="Obtener una lista de Autos", operation_id="Lista_de_Autos")
def get_autos( # Definimos los limites para devolver la lista paginada. 
    skip: int = Query(0, ge=0, description="Número de autos a saltar"),
    limit: int = Query(100, ge=1, le=1000, description="Número de autos a devolver"),
    servicio: AutoServiceInterface = Depends(get_auto_service) # DIP
) -> List[AutoResponse]:
    return servicio.get_autos(skip, limit) # Devolvemos la lista paginada.
# -----------------------------------------------------------------------------------

# -------------------------------- GET BY ID ----------------------------------------
# Definimos el endpoint: GET/autos/{auto_id}.
@router.get("/{auto_id}", response_model=AutoResponse, summary="Obtener un auto por su ID", operation_id="Obtener_un_Auto")
def get_auto( auto_id: int, 
    servicio: AutoServiceInterface = Depends(get_auto_service) ) -> AutoResponse:
    try:
        return servicio.get_auto_by_id(auto_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------

# ------------------------------- GET BY CHASIS -------------------------------------
# Definimos el endpoint: GET/autos/{nro_chasis}.
@router.get("/chasis/{nro_chasis}", response_model=AutoResponse, summary="Obtener un Auto por su chasis", operation_id="Obtener_Auto_por_Chasis")
def get_auto_by_chasis( nro_chasis: str,
    servicio: AutoServiceInterface = Depends(get_auto_service)) -> AutoResponse:
    try:
        return servicio.get_auto_by_chasis(nro_chasis)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------

# -------------------------------- PUT ----------------------------------------------
# Definimos el endpoint: PUT/autos/{auto_id}.
@router.put("/{auto_id}", response_model=AutoResponse, summary="Actualizar un Auto", operation_id="Actualizar_Auto")
def update_auto( auto_id: int, data: AutoUpdate,
    servicio: AutoServiceInterface = Depends(get_auto_service)) -> AutoResponse:
    try:
        return servicio.update_auto(nro_chasis, data)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
# ----------------------------------------------------------------------------------

# ---------------------------------- DELETE ----------------------------------------
# Definimos el endpoint: DELETE/autos/{auto_id}.
@router.delete("/{auto_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Borrar un Auto", operation_id="Borrar_Auto")
def delete_auto( auto_id: int,
    servicio: AutoServiceInterface = Depends(get_auto_service)) -> None:
    try:
        deleted = servicio.delete_auto(auto_id)
        if not deleted:
            raise Exception("No se pudo eliminar el auto")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
@router.get("/auto/{auto_id}", response_model=AutoResponseWithVentas, summary="Listar un Auto con todas sus ventas ", operation_id="Listar_Auto_con_Ventas")
def get_auto_with_ventas(auto_id: int, servicio: JoinServiceInterface = Depends(get_join_service)):
    result = servicio.get_auto_with_ventas(auto_id)

    if not result:
        raise HTTPException(status_code=404, detail="Auto no encontrado")

    return result
# ----------------------------------------------------------------------------------