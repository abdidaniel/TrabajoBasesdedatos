from dataclasses import dataclass
from typing import Optional


@dataclass
class ConfiguracionVO:
    id_confi: Optional[int] = None  # PK INT
    id_usuario: Optional[int] = None  # FK
    id_destino: Optional[int] = None  # FK
    id_visualizacion: Optional[int] = None  # FK
    id_vehiculo: Optional[int] = None  # FK
    colpass: Optional[bool] = None  # BOOL
    alertas_trafico: Optional[bool] = None
    idioma: Optional[str] = None  # BOOL
    navegacion: Optional[str] = None  # ('Evita Peajes', 'No Evita')
