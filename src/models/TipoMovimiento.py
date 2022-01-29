import json
from models.Estatus import Estatus

class TipoMovimiento:
    def __init__(self):
        self.tipoMovimientoId = 0
        self.descripcion = ''
        self.estatusId = 0
        self.estatus = Estatus()
    
    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)