import json
from models.ColorBootstrap import ColorBootstrap

class InstrumentoColorBootstrap:
    def __init__(self):
        self.instrumentoColorBootstrapId = 0
        self.instrumentoId = 0
        self.colorBootstrapId = 0
        self.colorBootstrap = ColorBootstrap()

    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)