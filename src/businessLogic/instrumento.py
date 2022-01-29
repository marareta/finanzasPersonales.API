from flask import jsonify
import DataAccess.instrumento

def ObtenerInstrumentosResumen():
    try:
        return DataAccess.instrumento.ObtenerInstrumentosResumen()
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


def ObtenerInstrumentosActivos():
    try:
        return DataAccess.instrumento.ObtenerInstrumentosActivos()
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


def ObtenerInstrumentoInformacionGeneral(obj):
    try:
        return DataAccess.instrumento.ObtenerInstrumentoInformacionGeneral(obj)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


def ValidarInstrumentoExistenteValorDelDia(obj):
    try:
        return DataAccess.instrumento.ValidarInstrumentoExistenteValorDelDia(obj)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


def GuardarInstrumentoValorDelDia(obj):
    try:
        return DataAccess.instrumento.GuardarInstrumentoValorDelDia(obj)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})

    
def ObtenerReporteGananciaPerdidaInversion():
    try:
        return DataAccess.instrumento.ObtenerReporteGananciaPerdidaInversion()
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})