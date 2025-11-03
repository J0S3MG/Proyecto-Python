import os
from fastapi import Depends
from Services.Interfaces.AutoInterface import AutoRepositoryInterface, AutoServiceInterface
from Repositories.AutoRepository import AutoRepository
from Services.AutoService import AutoService

# --------------------------------------------------- FACTORY --------------------------------------------------------------------------
# Este archivo cumple la funcion de una "Fabrica" (Solo hace Inyeccion de Dependencia).
# Farbica (Factory): Se llama “fábrica” porque el archivo produce (crea) objetos dependiendo del contexto.
# Con esto ayudamos a cumplir los principios SOLID, más concretamente el OCP.
# --------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------- AUTO FACTORY ---------------------------------------------------------------------
# Con este metodo realizamos la inyeccion de dependencia del Repositorio.
def get_auto_repository() -> AutoRepositoryInterface:
    return AutoRepository()# De esta manera da igual los cambios que hagamos en la implementacion que el resto seguira funcionando igual.

# En este caso hacemos la inyeccion de dependencia del Servicio.
def get_auto_service( repo: AutoRepositoryInterface = Depends(get_auto_repository)) -> AutoServiceInterface:
    return AutoService(repo) # Le pasamos el Repositorio para que se inyeccte en la clase concreta.
# ----------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------- VENTA FACTORY ---------------------------------------------------------------------
#def get_venta_repository() -> VentaRepositoryInterface:# Con este metodo realizamos la inyeccion de dependencia del Repositorio.
#    return VentaRepositoryInMemory()

#def get_venta_service(repo: VentaRepositoryInterface = Depends(get_venta_repository)) -> VentaServiceInterface:
#    return VentaService(repo)
# ----------------------------------------------------------------------------------------------------------------------------------------


