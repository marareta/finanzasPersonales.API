import json

class Saldo:
    def __init__(self):
        self.saldoId = 0
        self.instrumentoId = 0
        self.monto = 0

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)