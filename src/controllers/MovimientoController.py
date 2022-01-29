import flask
from flask import Flask, jsonify, request
from config import config
import json
from models.Error import Error
from models.Movimiento import Movimiento
from models.ReporteGeneral import ReporteGeneral

from models.Usuario import Usuario
import businessLogic.usuario
import businessLogic.instrumento
import businessLogic.movimiento
import businessLogic.tipoMovimiento

import jsonpickle
from decimal import Decimal

movimientoController = flask.Blueprint('movimientoController', __name__)

@movimientoController.route('/api/Movimiento/ObtenerReporteGeneralDeInversiones', methods=['POST'])
def ObtenerReporteGeneralDeInversiones():
    try:
        #jsonpickle.set_preferred_backend('simplejson')
        retorno = ReporteGeneral()
        retorno = businessLogic.movimiento.ObtenerReporteGeneralDeInversiones()
        
        return (retorno.to_json())
        
    except Exception as ex:
        return Error("Error", False, ex.args)


@movimientoController.route('/api/Movimiento/ObtenerReporteGananciaPerdidaInversion', methods=['POST'])
def ObtenerReporteGananciaPerdidaInversion():
    try:
        retorno = ReporteGeneral()
        retorno = businessLogic.instrumento.ObtenerReporteGananciaPerdidaInversion()
        
        return (retorno.to_json())
        
    except Exception as ex:
        return Error("Error", False, ex.args)


@movimientoController.route('/api/Movimiento/ObtenerInversionPorEtiqueta', methods=['POST'])
def ObtenerInversionPorEtiqueta():
    try:
        retorno = businessLogic.movimiento.ObtenerInversionPorEtiqueta()

        return jsonpickle.encode(retorno, unpicklable=False)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


@movimientoController.route('/api/Movimiento/ObtenerTipoMovimientosActivos', methods=['POST'])
def ObtenerTipoMovimientosActivos():
    try:
        retorno = businessLogic.tipoMovimiento.ObtenerTipoMovimientosActivos()

        return jsonpickle.encode(retorno, unpicklable=False)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})



@movimientoController.route('/api/Movimiento/GuardarMovimiento', methods=['POST'])
def GuardarMovimiento():
    try:
        data = str(request.get_json()).replace("'", '"')
        python_dict = json.loads(data)

        obj = Movimiento()
        obj.movimientoId = python_dict['movimientoId']
        obj.tipoMovimientoId = python_dict['tipoMovimientoId']
        obj.fechaMovimiento = python_dict['fechaMovimiento']
        obj.instrumentoId = python_dict['instrumentoId']
        obj.monto = python_dict['monto']
        obj.esFondoEmergencias = python_dict['esFondoEmergencias']
        obj.movimientosEtiquetas = python_dict['movimientosEtiquetas']
        obj.cantidadAcciones = python_dict['cantidadAcciones']
        obj.comentarios = python_dict['comentarios']
        obj.usuario.usuarioId = python_dict['usuario']['usuarioId']

        retorno = businessLogic.movimiento.GuardarMovimiento(obj)

        return jsonpickle.encode(retorno, unpicklable=False)
        #return(jsonify({"sad":"sada"}))
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'error': ex.args})


