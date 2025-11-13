import os
from fastapi import Depends
from sqlmodel import Session
from database import get_session
from Services.Interfaces.AutoInterface import AutoRepositoryInterface, AutoServiceInterface
from Repositories.AutoRepository import AutoRepository
from Services.AutoService import AutoService
from Services.Interfaces.VentaInterface import VentaRepositoryInterface, VentaServiceInterface
from Repositories.VentaRepository import VentaRepository
from Services.VentaService import VentaService
from Services.Interfaces.JoinInterface import JoinServiceInterface
from Services.JoinService import JoinService

# --------------------------------------------------- FACTORY --------------------------------------------------------------------------
# Este archivo cumple la funcion de una "Fabrica" (Solo hace Inyeccion de Dependencia).
# Farbica (Factory): Se llama “fábrica” porque el archivo produce (crea) objetos dependiendo del contexto.
# Con esto ayudamos a cumplir los principios SOLID, más concretamente el OCP.
# --------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------- AUTO FACTORY ---------------------------------------------------------------------
# Con este metodo realizamos la inyeccion de dependencia del Repositorio.
def get_auto_repository(session: Session = Depends(get_session)) -> AutoRepositoryInterface:
    return AutoRepository(session)# De esta manera da igual los cambios que hagamos en la implementacion que el resto seguira funcionando igual.

# En este caso hacemos la inyeccion de dependencia del Servicio.
def get_auto_service(auto_repo: AutoRepositoryInterface = Depends(get_auto_repository)) -> AutoServiceInterface:
    return AutoService(auto_repo) # Le pasamos el Repositorio para que se inyeccte en la clase concreta.
# ----------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------- VENTA FACTORY ---------------------------------------------------------------------
# Con este metodo realizamos la inyeccion de dependencia del Repositorio.
def get_venta_repository(session: Session = Depends(get_session)) -> VentaRepositoryInterface:
    return VentaRepository(session)

# En este caso hacemos la inyeccion de dependencia del Servicio.
def get_venta_service(venta_repo: VentaRepositoryInterface = Depends(get_venta_repository)) -> VentaServiceInterface:
    return VentaService(venta_repo)
# ----------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------- JOIN FACTORY -----------------------------------------------------------------------
def get_join_service(auto_repo: AutoRepositoryInterface = Depends(get_auto_repository), venta_repo: VentaRepositoryInterface = Depends(get_venta_repository)) -> VentaServiceInterface:
    return JoinService(auto_repo,venta_repo)
# ----------------------------------------------------------------------------------------------------------------------------------------


