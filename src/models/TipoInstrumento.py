import json
from models.Estatus import Estatus
from models.Plataforma import Plataforma

class TipoInstrumento:
    def __init__(self):
        self.tipoInstrumentoId = 0
        self.estatusId = 0
        self.descripcion = ''
        self.estatus = Estatus()
        self.plataforma = Plataforma()

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)