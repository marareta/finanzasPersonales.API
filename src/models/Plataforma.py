import json
from models.Estatus import Estatus

class Plataforma:
    def __init__(self):
        self.plataformaId = 0
        self.estatusId = 0
        self.descripcion = ''
        self.estatus = Estatus()
        self.tiposInstrumentos = []

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)