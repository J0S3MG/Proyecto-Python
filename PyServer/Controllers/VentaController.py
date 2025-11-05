from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from Models.Join import VentaResponseWithAuto
from Models.Venta import VentaCreate, VentaUpdate, VentaResponse
from Services.Interfaces.VentaInterface import VentaServiceInterface # Interfaz de servicio
from Services.Interfaces.JoinInterface import JoinServiceInterface
from deps import get_venta_service, get_join_service  # Inyección de dependencia

# Definimos la ruta base para los endpoints de venta
router = APIRouter(prefix="/ventas", tags=["Ventas"])

# -------------------------------- POST ---------------------------------------------
# POST /ventas - Crear nueva venta
@router.post("/", response_model=VentaResponse, status_code=status.HTTP_201_CREATED, summary="Crea una Venta", operation_id="Crear_Venta")
def create_venta( nuevo: VentaCreate,
    servicio: VentaServiceInterface = Depends(get_venta_service)) -> VentaResponse:
    try:
        return servicio.create_venta(nuevo)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------


# -------------------------------- GET ALL ------------------------------------------
# GET /ventas - Listar ventas con paginación
@router.get("/", response_model=List[VentaResponse], summary="Obtener una lista de ventas", operation_id="Lista_de_Ventas")
def get_ventas(
    skip: int = Query(0, ge=0, description="Número de ventas a saltar"),
    limit: int = Query(100, ge=1, le=1000, description="Número de ventas a devolver"),
    servicio: VentaServiceInterface = Depends(get_venta_service)
    ) -> List[VentaResponse]:
    return servicio.get_ventas(skip, limit)
# -----------------------------------------------------------------------------------


# -------------------------------- GET BY ID ----------------------------------------
# GET /ventas/{venta_id} - Obtener venta por ID
@router.get("/{venta_id}", response_model=VentaResponse, summary="Obtener una venta por ID", operation_id="Obtener_una_Venta")
def get_venta_by_id( venta_id: int,
    servicio: VentaServiceInterface = Depends(get_venta_service)) -> VentaResponse:
    try:
        return servicio.get_venta_by_id(venta_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------


# ------------------------------- GET BY AUTO ---------------------------------------
# GET /ventas/auto/{auto_id} - Ventas de un auto específico
@router.get("/auto/{auto_id}", response_model=List[VentaResponse], summary="Obtener una lista de ventas de un auto", operation_id="Ventas_de_un_Auto")
def get_ventas_by_auto( auto_id: int, servicio: VentaServiceInterface = Depends(get_venta_service)) -> List[VentaResponse]:
    try:
        return servicio.get_ventas_by_auto(auto_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------


# ----------------------------- GET BY COMPRADOR ------------------------------------
# GET /ventas/comprador/{nombre} - Ventas por nombre de comprador
@router.get("/comprador/{nombre}", response_model=List[VentaResponse], summary="Obtener una lista de ventas de un comprador", operation_id="Ventas_de_un_Comprador")
def get_ventas_by_comprador(nombre: str,
    servicio: VentaServiceInterface = Depends(get_venta_service)) -> List[VentaResponse]:
    try:
        return servicio.get_ventas_by_comprador(nombre)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------


# -------------------------------- PUT ----------------------------------------------
# PUT /ventas/{venta_id} - Actualizar venta
@router.put("/{venta_id}", response_model=VentaResponse, summary="Actualizar una venta", operation_id="Actualizar_Venta")
def update_venta( venta_id: int, data: VentaUpdate,
    servicio: VentaServiceInterface = Depends(get_venta_service)) -> VentaResponse:
    try:
        return servicio.update_venta(venta_id, data)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------


# -------------------------------- DELETE -------------------------------------------
# DELETE /ventas/{venta_id} - Eliminar venta
@router.delete("/{venta_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Borrar una Venta", operation_id="Borrar_Venta")
def delete_venta( venta_id: int,
    servicio: VentaServiceInterface = Depends(get_venta_service)) -> None:
    try:
        deleted = servicio.delete_venta(venta_id)
        if not deleted:
            raise Exception("No se pudo eliminar la venta")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------
@router.get("/venta/{venta_id}", response_model=VentaResponseWithAuto, summary="Listar una venta con su auto", operation_id="Listar_Venta_con_Auto")
def get_venta_with_auto(venta_id: int, servicio: JoinServiceInterface = Depends(get_join_service)):
    result = servicio.get_venta_with_auto(venta_id)

    if not result:
        raise HTTPException(status_code=404, detail="Venta no encontrada")

    return result
# -----------------------------------------------------------------------------------