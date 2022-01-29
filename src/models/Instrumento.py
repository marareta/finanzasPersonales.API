import json
from models.Estatus import Estatus
from models.TipoInstrumento import TipoInstrumento
from models.InstrumentoPorcentajeObjetivo import InstrumentoPorcentajeObjetivo
from models.InstrumentoFondoEmergencia import InstrumentoFondoEmergencia
from models.Saldo import Saldo
from models.InstrumentoColorBootstrap import InstrumentoColorBootstrap

class Instrumento:
    def __init__(self):
        self.instrumentoId = 0
        self.estatusId = 0
        self.descripcion = ''
        self.descripcionLarga = ''
        self.tipoInstrumentoId = 0
        self.estatus = Estatus()
        self.tipoInstrumento = TipoInstrumento()
        self.instrumentoPorcentajeObjetivo = InstrumentoPorcentajeObjetivo()
        self.instrumentoFondoEmergencia = InstrumentoFondoEmergencia()
        self.movimientos = []
        self.saldo = Saldo()
        self.instrumentoPorcentajeReal = InstrumentoPorcentajeObjetivo()
        self.instrumentosValoresDelDia = []
        self.instrumentoColorBootstrap = InstrumentoColorBootstrap()

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)
