import json
from datetime import date
from models.Instrumento import Instrumento
from models.Estatus import Estatus
from models.Usuario import Usuario
from models.TipoMovimiento import TipoMovimiento
import jsonpickle
import decimal

class Movimiento:
    def __init__(self):
        self.movimientoId = 0
        self.tipoMovimientoId = 0
        self.fechaGuardado = date.today()
        self.fechaMovimiento = date.today()
        self.fechaUltimaActualizacion = date.today()
        self.instrumentoId = 0
        self.monto = decimal.Decimal(0)
        self.esFondoEmergencias = 0
        self.estatusId = 0
        self.usuarioId = 0
        self.comentarios = 0
        self.cantidadAcciones = 0
        self.tipoMovimiento = TipoMovimiento()
        self.instrumento = Instrumento()
        self.estatus = Estatus()
        self.movimientosEtiquetas = []
        self.usuario = Usuario()

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)

    def to_json(self):
        return jsonpickle.dumps(self, unpicklable=False)