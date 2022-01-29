import flask
from flask import Flask, jsonify, request
from config import config
import json
import businessLogic.instrumento
import funciones
import jsonpickle

from models.Instrumento import Instrumento
from models.InstrumentoValorDelDia import InstrumentoValorDelDia

instrumentoController = flask.Blueprint('instrumentoController', __name__)

@instrumentoController.route('/api/Instrumento/ObtenerInstrumentosResumen', methods=['POST'])
def ObtenerInstrumentosResumen():
    try:
        retorno = businessLogic.instrumento.ObtenerInstrumentosResumen()
        return jsonpickle.encode(retorno, unpicklable=False)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


@instrumentoController.route('/api/Instrumento/ObtenerInstrumentosActivos', methods=['POST'])
def ObtenerInstrumentosActivos():
    try:
        retorno = businessLogic.instrumento.ObtenerInstrumentosActivos()
        return jsonpickle.encode(retorno, unpicklable=False)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


@instrumentoController.route('/api/Instrumento/ObtenerInstrumentoInformacionGeneral', methods=['POST'])
def ObtenerInstrumentoInformacionGeneral():
    try:
        data = str(request.get_json()).replace("'", '"')
        python_dict = json.loads(data)

        obj = Instrumento()
        obj.instrumentoId = python_dict['instrumentoId']

        retorno = businessLogic.instrumento.ObtenerInstrumentoInformacionGeneral(obj)
        return jsonpickle.encode(retorno, unpicklable=False)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


@instrumentoController.route('/api/Instrumento/ValidarInstrumentoExistenteValorDelDia', methods=['POST'])
def ValidarInstrumentoExistenteValorDelDia():
    try:
        data = str(request.get_json()).replace("'", '"')
        python_dict = json.loads(data)

        obj = InstrumentoValorDelDia()
        obj.instrumentoValorDelDiaId = python_dict['instrumentoValorDelDiaId']
        obj.instrumentoId = python_dict['instrumentoId']
        obj.fecha = python_dict['fecha']
        
        retorno = businessLogic.instrumento.ValidarInstrumentoExistenteValorDelDia(obj)
        return jsonpickle.encode(retorno, unpicklable=False)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


@instrumentoController.route('/api/Instrumento/GuardarInstrumentoValorDelDia', methods=['POST'])
def GuardarInstrumentoValorDelDia():
    try:
        data = str(request.get_json()).replace("'", '"')
        python_dict = json.loads(data)

        obj = InstrumentoValorDelDia()
        obj.instrumentoValorDelDiaId = python_dict['instrumentoValorDelDiaId']
        obj.instrumentoId = python_dict['instrumentoId']
        obj.fecha = python_dict['fecha']
        obj.valor = python_dict['valor']
        
        retorno = businessLogic.instrumento.GuardarInstrumentoValorDelDia(obj)
        return jsonpickle.encode(retorno, unpicklable=False)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})