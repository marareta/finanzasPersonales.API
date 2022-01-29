import json

from models.TipoDato import TipoDato

class Caracteristica:
    def __init__(self):
        self.caracteristicaId = 0
        self.descripcion = ''
        self.tipoDatoId = 0
        self.prospectoCaracteristicas = []
        self.tipoDato = TipoDato()

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)