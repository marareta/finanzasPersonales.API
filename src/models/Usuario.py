from models.Estatus import Estatus
import json

from models.UsuarioCredenciales import UsuarioCredenciales
from models.UsuarioDatosGenerales import UsuarioDatosGenerales

class Usuario:
    def __init__(self):
        self.usuarioId = 0
        self.estatusId = 0
        self.usuarioCredenciales = UsuarioCredenciales()
        self.usuarioDatosGenerales = UsuarioDatosGenerales()
        self.estatus = Estatus()

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)