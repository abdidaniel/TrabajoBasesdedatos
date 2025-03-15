from dataclasses import dataclass
from typing import Optional

@dataclass
class ConfiguracionVO:
    id_confi: Optional[int] = None 
    fk_usuario: Optional[int] = None  
    fk_destino: Optional[int] = None  
    fk_visualizacion: Optional[int] = None  
    fk_vehiculo: Optional[int] = None 
    colpass: Optional[bool] = None  
    navegacion_check: Optional[str] = None 