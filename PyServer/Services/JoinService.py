from typing import Optional, List
from Services.Interfaces.JoinInterface import JoinServiceInterface
from Services.Interfaces.AutoInterface import AutoRepositoryInterface
from Services.Interfaces.VentaInterface import VentaRepositoryInterface
from Models.Join import AutoResponseWithVentas, VentaResponseWithAuto
from Models.Auto import AutoResponse
from Models.Venta import VentaResponse

class JoinService(JoinServiceInterface):

    def __init__(self, auto_repo: AutoRepositoryInterface, venta_repo: VentaRepositoryInterface):
        self.auto_repo = auto_repo
        self.venta_repo = venta_repo


    # ----------------------------------------------------------------
    def get_auto_with_ventas(self, auto_id: int) -> Optional[AutoResponseWithVentas]:
        """Retorna un auto con todas sus ventas"""
        auto = self.auto_repo.get_by_id(auto_id)
        if not auto:
            return None
    
        ventas = self.venta_repo.get_by_auto_id(auto_id)
        # Convertimos cada venta a DTO VentaResponse
        ventas_response = [
                VentaResponse(
                id=v.id,
                nom_comprador=v.nom_comprador,
                precio=v.precio,
                fecha_venta=v.fecha_venta,
                auto_id=v.auto_id
            )
            for v in ventas
        ]

        return AutoResponseWithVentas(
            id=auto.id,
            marca=auto.marca,
            modelo=auto.modelo,
            ano=auto.ano,
            nro_chasis=auto.nro_chasis,
            ventas=ventas_response
        )
    # ----------------------------------------------------------------


    # ----------------------------------------------------------------
    def get_venta_with_auto(self, venta_id: int) -> Optional[VentaResponseWithAuto]:
        """Retorna una venta con la información del auto relacionado"""

        venta = self.venta_repo.get_by_id(venta_id)
        if not venta:
            return None

        auto = self.auto_repo.get_by_id(venta.auto_id)

        return VentaResponseWithAuto(
            id=venta.id,
            nom_comprador=venta.nom_comprador,
            precio=venta.precio,
            fecha_venta=venta.fecha_venta,
            auto_id=venta.auto_id,
            auto=auto if auto else None  # type: ignore
        )
    # ----------------------------------------------------------------