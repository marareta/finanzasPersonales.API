import flask
from flask import Flask, jsonify, request
from config import config
import json

from models.Etiqueta import Etiqueta
import businessLogic.etiqueta
import jsonpickle

etiquetaController = flask.Blueprint('etiquetaController', __name__)

@etiquetaController.route('/api/Etiqueta/ObtenerEtiquetasActivas', methods=['POST'])
def ObtenerEstatusPorTipoObjeto():
    try:
        retorno = businessLogic.etiqueta.ObtenerEtiquetasActivas()

        return jsonpickle.encode(retorno, unpicklable=False)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


@etiquetaController.route('/api/Etiqueta/ObtenerEtiquetas', methods=['POST'])
def ObtenerEtiquetas():
    try:
        retorno = businessLogic.etiqueta.ObtenerEtiquetas()

        return jsonpickle.encode(retorno, unpicklable=False)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


@etiquetaController.route('/api/Etiqueta/ObtenerEtiquetaPorId', methods=['POST'])
def ObtenerEtiquetaPorId():
    try:
        data = str(request.get_json()).replace("'", '"')
        python_dict = json.loads(data)

        obj = Etiqueta()
        obj.etiquetaId = python_dict['etiquetaId']

        retorno = businessLogic.etiqueta.ObtenerEtiquetaPorId(obj)

        return jsonpickle.encode(retorno, unpicklable=False)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


@etiquetaController.route('/api/Etiqueta/ValidarEtiqueta', methods=['POST'])
def ValidarEtiqueta():
    try:
        data = str(request.get_json()).replace("'", '"')
        python_dict = json.loads(data)

        obj = Etiqueta()
        obj.etiquetaId = python_dict['etiquetaId']
        obj.descripcion = python_dict['descripcion']

        retorno = businessLogic.etiqueta.ValidarEtiqueta(obj)

        return jsonpickle.encode(retorno, unpicklable=False)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


@etiquetaController.route('/api/Etiqueta/ValidarEtiquetaPorObjeto', methods=['POST'])
def ValidarEtiquetaPorObjeto():
    try:
        data = str(request.get_json()).replace("'", '"')
        python_dict = json.loads(data)

        obj = Etiqueta()
        obj.etiquetaId = python_dict['etiquetaId']
        obj.descripcion = python_dict['descripcion']

        msj = businessLogic.etiqueta.ValidarEtiqueta(obj)
        retorno = Etiqueta()
        if(msj != ""):
            retorno.etiquetaId = 1

        return jsonpickle.encode(retorno, unpicklable=False)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


@etiquetaController.route('/api/Etiqueta/GuardarEiqueta', methods=['POST'])
def GuardarEiqueta():
    try:
        data = str(request.get_json()).replace("'", '"')
        python_dict = json.loads(data)

        obj = Etiqueta()
        obj.etiquetaId = python_dict['etiquetaId']
        obj.descripcion = python_dict['descripcion']
        obj.estatusId = python_dict['estatusId']

        retorno = businessLogic.etiqueta.GuardarEiqueta(obj)

        return jsonpickle.encode(retorno, unpicklable=False)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})
