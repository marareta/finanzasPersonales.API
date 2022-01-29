import json
from models.Estatus import Estatus

class Etiqueta:
    def __init__(self):
        self.etiquetaId = 0
        self.estatusId = 0
        self.descripcion = ''
        self.estatus = Estatus()

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)