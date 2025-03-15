from dataclasses import dataclass
from typing import Optional

@dataclass
class ConfiguracionVO:
    id_confi: Optional[int] = None  # PK INT
    fk_usuario: Optional[int] = None  # FK
    fk_destino: Optional[int] = None  # FK
    fk_visualizacion: Optional[int] = None  # FK
    fk_vehiculo: Optional[int] = None  # FK
    colpass: Optional[bool] = None  # BOOL
    navegacion_check: Optional[str] = None  # ('Evita Peajes', 'No Evita')