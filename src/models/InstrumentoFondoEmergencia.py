import json

class InstrumentoFondoEmergencia:
    def __init__(self):
        self.instrumentoFondoEmergenciaId = 0
        self.instrumentoId = 0
        self.esFondoEmergencia = 0

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)