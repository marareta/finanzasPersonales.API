from flask import jsonify
import DataAccess.tipoMovimiento

def ObtenerTipoMovimientosActivos():
    try:
        return DataAccess.tipoMovimiento.ObtenerTipoMovimientosActivos()
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})