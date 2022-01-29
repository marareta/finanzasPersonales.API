import json

class InstrumentoPorcentajeObjetivo:
    def __init__(self):
        self.instrumentoPorcentajeObjetivoId = 0
        self.instrumentoId = 0
        self.porcentaje = 0

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)