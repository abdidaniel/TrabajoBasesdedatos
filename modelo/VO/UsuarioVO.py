from dataclasses import dataclass

@dataclass 
class UsuarioVO:
    nombre : str
    apellido : str
    correo : str
    sexo : str