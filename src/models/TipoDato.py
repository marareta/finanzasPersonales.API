import json

class TipoDato:
    def __init__(self):
        self.tipoDatoId = 0
        self.descripcion = ''

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)