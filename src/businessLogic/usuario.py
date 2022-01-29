from flask import jsonify
import DataAccess.usuario

def ValidaUsuarioLogin(usuario):
    try:
        return DataAccess.usuario.ValidaUsuarioLogin(usuario)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})