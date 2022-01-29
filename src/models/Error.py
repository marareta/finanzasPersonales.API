import json

class Error:
    def __init__(self, mensaje, exito, error):
        self.mensaje = mensaje
        self.exito = exito
        self.error = error
    
    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)

    