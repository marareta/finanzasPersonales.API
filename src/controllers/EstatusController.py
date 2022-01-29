import flask
from flask import Flask, jsonify, request
from config import config
import json

from models.Estatus import Estatus
from models.TipoObjeto import TipoObjeto
import businessLogic.estatus
import jsonpickle

estatusController = flask.Blueprint('estatusController', __name__)

@estatusController.route('/api/Estatus/ObtenerEstatusPorTipoObjeto', methods=['POST'])
def ObtenerEstatusPorTipoObjeto():
    try:
        data = str(request.get_json()).replace("'", '"')
        python_dict = json.loads(data)

        obj = TipoObjeto()
        obj.descripcion = python_dict['descripcion']

        retorno = businessLogic.estatus.ObtenerEstatusPorTipoObjeto(obj)

        return jsonpickle.encode(retorno, unpicklable=False)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})

