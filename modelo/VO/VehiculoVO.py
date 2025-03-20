from dataclasses import dataclass
from typing import Optional


@dataclass
class VehiculoVO:
    id_vehiculo: Optional[int] = None
    tipo_vehiculo: Optional[str] = None
    tipo_combustible: Optional[str] = None
    matricula: Optional[str] = None
    fk_usuario: Optional[int] = None
