from dataclasses import dataclass
from typing import Optional

@dataclass
class DireccionVO:
    id_direccion: Optional[int] = None 
    nombre: Optional[str] = None  
    latitud: Optional[float] = None  
    longitud: Optional[float] = None 