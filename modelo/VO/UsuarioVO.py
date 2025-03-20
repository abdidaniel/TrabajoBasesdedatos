from dataclasses import dataclass
from typing import Optional


@dataclass
class UsuarioVO:
    ID_usuario: Optional[int] = None
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    correo:  Optional[str] = None
    sexo:  Optional[str] = None
