import json
import decimal
from pickletools import decimalnl_long
import jsonpickle
from datetime import date

class ReporteGeneral:
    def __init__(self):
        self.montoTotal = decimal.Decimal(0)
        self.fondoEmergencias = decimal.Decimal(0)
        self.montoInvertido = decimal.Decimal(0)
        self.fecha = date.today()
        self.porcentaje = decimal.Decimal(0)

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)


    def to_json(self):
        return jsonpickle.dumps(self, unpicklable=False)