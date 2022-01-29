from flask import jsonify
import DataAccess.estatus

def ObtenerEstatusPorTipoObjeto(obj):
    try:
        return DataAccess.estatus.ObtenerEstatusPorTipoObjeto(obj)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})