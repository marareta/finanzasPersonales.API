import json

from models.Etiqueta import Etiqueta
from models.Movimiento import Movimiento

class MovimientoEtiqueta:
    def __init__(self):
        self.movimientoEtiquetaId = 0
        self.movimientoId = 0
        self.etiquetaId = 0
        self.etiqueta = Etiqueta()
        self.movimiento = Movimiento()

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)