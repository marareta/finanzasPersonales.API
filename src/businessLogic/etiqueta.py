from flask import jsonify
import DataAccess.etiqueta

def ObtenerEtiquetasActivas():
    try:
        return DataAccess.etiqueta.ObtenerEtiquetasActivas()
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


def ObtenerEtiquetas():
    try:
        return DataAccess.etiqueta.ObtenerEtiquetas()
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


def ObtenerEtiquetaPorId(obj):
    try:
        return DataAccess.etiqueta.ObtenerEtiquetaPorId(obj)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


def ValidarEtiqueta(obj):
    try:
        return DataAccess.etiqueta.ValidarEtiqueta(obj)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


def GuardarEiqueta(obj):
    try:
        return DataAccess.etiqueta.GuardarEiqueta(obj)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})