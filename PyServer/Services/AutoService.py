from typing import List
from Services.Interfaces.AutoInterface import AutoRepositoryInterface, AutoServiceInterface# Le pasamos ambas interfaces.
from Models.Auto import AutoCreate, AutoUpdate, AutoResponse

class AutoService(AutoServiceInterface):
	"""Implementación del AutoServiceInterface"""

	def __init__(self, repo: AutoRepositoryInterface):
		self.repo = repo # Le pasamos la interfaz de repositorio (Esto hara la Inyeccion de Dependencia).
	
	# ------------------------------------ CREATE ------------------------------------
	def create_auto(self, nuevo: AutoCreate) -> AutoResponse:
		"""Crea un auto"""
		new_auto = self.repo.create(nuevo)
		return AutoResponse.model_validate(new_auto)
	# --------------------------------------------------------------------------------


	# ------------------------------------ GET ALL -----------------------------------
	def get_autos(self, skip: int, limit: int) -> List[AutoResponse]:
		"""Devuelve una lista paginada de autos"""
		autos = self.repo.get_all(skip=skip, limit=limit)
		return [AutoResponse.model_validate(auto) for auto in autos]
	# --------------------------------------------------------------------------------


	# ------------------------------------ GET BY ID ---------------------------------
	def get_auto_by_id(self, auto_id: int) -> AutoResponse:
		"""Devuelve un auto por su ID"""
		auto = self.repo.get_by_id(auto_id)
		if not auto:
			raise ValueError(f"Auto con id {auto_id} no encontrado")
		return AutoResponse.model_validate(auto)
	# --------------------------------------------------------------------------------


	# ---------------------------------- GET BY CHASIS -------------------------------
	def get_auto_by_chasis(self, nro_chasis: str) -> AutoResponse:
		"""Devuelve un auto por su Nro de Chasis"""
		auto = self.repo.get_by_chasis(nro_chasis)
		if not auto:
			raise ValueError(f"Auto con chasis {nro_chasis} no encontrado")
		return AutoResponse.model_validate(auto)
	# --------------------------------------------------------------------------------


	# ------------------------------------ UPDATE ------------------------------------
	def update_auto(self, auto_id: int, auto_update: AutoUpdate) -> AutoResponse:
		"""Actualiza un auto por su Nro de Chasis"""
		auto_actualizado = self.repo.update(auto_id, auto_update)
		if not auto_actualizado:
			raise ValueError(f"No se pudo actualizar el auto con chasis {auto_id}")
		return AutoResponse.model_validate(auto_actualizado)
	# --------------------------------------------------------------------------------


	# ------------------------------------ DELETE ------------------------------------
	def delete_auto(self, auto_id: int) -> bool:
		"""Elimina un auto por su ID"""
		eliminado = self.repo.delete(auto_id)
		if not eliminado:
			raise ValueError(f"No se pudo eliminar el auto con id {auto_id}")
		return True
	# --------------------------------------------------------------------------------