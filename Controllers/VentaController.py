from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from Models.Venta import VentaCreate, VentaUpdate, VentaResponse
from Services.Interfaces.VentaInterface import VentaServiceInterface  # Interfaz de servicio
from deps import get_venta_service  # Inyección de dependencia

# Definimos la ruta base para los endpoints de venta
router = APIRouter(prefix="/ventas", tags=["Ventas"])

# -------------------------------- POST ---------------------------------------------
# POST /ventas - Crear nueva venta
@router.post("/", response_model=VentaResponse, status_code=status.HTTP_201_CREATED, summary="Crear una venta", operation_id="Crear Venta")
def create_venta( nuevo: VentaCreate,
    service: VentaServiceInterface = Depends(get_venta_service)) -> VentaResponse:
    try:
        return service.create_venta(nuevo)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------


# -------------------------------- GET ALL ------------------------------------------
# GET /ventas - Listar ventas con paginación
@router.get("/", response_model=List[VentaResponse])
def get_ventas(
    skip: int = Query(0, ge=0, description="Número de ventas a saltar"),
    limit: int = Query(100, ge=1, le=1000, description="Número de ventas a devolver"),
    service: VentaServiceInterface = Depends(get_venta_service)
    ) -> List[VentaResponse]:
    return service.get_ventas(skip, limit)
# -----------------------------------------------------------------------------------


# -------------------------------- GET BY ID ----------------------------------------
# GET /ventas/{venta_id} - Obtener venta por ID
@router.get("/{venta_id}", response_model=VentaResponse)
def get_venta_by_id( venta_id: int,
    service: VentaServiceInterface = Depends(get_venta_service)) -> VentaResponse:
    try:
        return service.get_venta_by_id(venta_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------


# ------------------------------- GET BY AUTO ---------------------------------------
# GET /ventas/auto/{auto_id} - Ventas de un auto específico
@router.get("/auto/{auto_id}", response_model=List[VentaResponse])
def get_ventas_by_auto( auto_id: int,
    skip: int = Query(0, ge=0, description="Número de ventas a saltar"),
    limit: int = Query(100, ge=1, le=1000, description="Número de ventas a devolver"),
    service: VentaServiceInterface = Depends(get_venta_service)) -> List[VentaResponse]:
    try:
        return service.get_ventas_by_auto(auto_id, skip, limit)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------


# ----------------------------- GET BY COMPRADOR ------------------------------------
# GET /ventas/comprador/{nombre} - Ventas por nombre de comprador
@router.get("/comprador/{nombre}", response_model=List[VentaResponse])
def get_ventas_by_comprador(nombre: str,
    service: VentaServiceInterface = Depends(get_venta_service)) -> List[VentaResponse]:
    try:
        return service.get_ventas_by_comprador(nombre)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------


# -------------------------------- PUT ----------------------------------------------
# PUT /ventas/{venta_id} - Actualizar venta
@router.put("/{venta_id}", response_model=VentaResponse)
def update_venta( venta_id: int, data: VentaUpdate,
    service: VentaServiceInterface = Depends(get_venta_service)) -> VentaResponse:
    try:
        return service.update_venta(venta_id, data)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------


# -------------------------------- DELETE -------------------------------------------
# DELETE /ventas/{venta_id} - Eliminar venta
@router.delete("/{venta_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_venta( venta_id: int,
    service: VentaServiceInterface = Depends(get_venta_service)) -> None:
    try:
        deleted = service.delete_venta(venta_id)
        if not deleted:
            raise Exception("No se pudo eliminar la venta")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
# -----------------------------------------------------------------------------------