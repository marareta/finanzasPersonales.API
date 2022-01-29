import json
from datetime import date
from models.Instrumento import Instrumento

class InstrumentoValorDelDia:
    def __init__(self):
        self.instrumentoValorDelDiaId = 0
        self.instrumentoId = 0
        self.valor = 0
        self.fecha = date.today()
        self.instrumento = Instrumento()

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)