import json

class UsuarioDatosGenerales:
    def __init__(self):
        self.usuarioDatosGeneralesId = 0
        self.usuarioId = 0
        self.nombres = ''
        self.apellidoPaterno = ''
        self.apellidoMaterno = ''

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)