import json


class UsuarioCredenciales:
    def __init__(self):
        self.usuarioCredencialesId = 0
        self.usuarioId = 0
        self.nombreUsuario = ''
        self.password = ''

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)