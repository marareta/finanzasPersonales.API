import flask
from flask import Flask, jsonify, request
from config import config
import json

from models.Usuario import Usuario
import businessLogic.usuario

usuarioController = flask.Blueprint('usuarioController', __name__)

@usuarioController.route('/api/Usuario/ValidaUsuarioLogin', methods=['POST'])
def ValidaUsuarioLogin():
    try:
        data = str(request.get_json()).replace("'", '"')
        python_dict = json.loads(data)

        usuario = Usuario()
        usuario.usuarioCredenciales.nombreUsuario = python_dict['nombreUsuario']
        usuario.usuarioCredenciales.password = python_dict['password']

        retorno = businessLogic.usuario.ValidaUsuarioLogin(usuario)

        return (retorno.toJSON())
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})

