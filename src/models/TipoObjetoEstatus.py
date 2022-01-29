import json
from models.TipoObjeto import TipoObjeto
from models.Estatus import Estatus

class TipoObjetoEstatus:
    def __init__(self):
        self.tipoObjetoEstatusId = 0
        self.tipoObjetoId = 0
        self.estatusId = 0
        self.tipoObjeto = TipoObjeto()
        self.estatus = Estatus()
    
    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)