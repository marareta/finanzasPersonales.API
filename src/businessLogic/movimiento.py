from flask import jsonify
import DataAccess.movimiento

def ObtenerReporteGeneralDeInversiones():
    try:
        return DataAccess.movimiento.ObtenerReporteGeneralDeInversiones()
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


def ObtenerInversionPorEtiqueta():
    try:
        return DataAccess.movimiento.ObtenerInversionPorEtiqueta()
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


def GuardarMovimiento(obj):
    try:
        etiquetas = ''
        return DataAccess.movimiento.GuardarMovimiento(obj, etiquetas)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})