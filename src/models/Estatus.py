import json

class Estatus:
    def __init__(self):
        self.estatusId = 0
        self.descripcion = ''
    
    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)

    