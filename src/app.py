from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from config import config
import json
from types import SimpleNamespace
from collections import namedtuple
from controllers.UsuarioController import usuarioController
from controllers.InstrumentoController import instrumentoController
from controllers.EstatusController import estatusController
from controllers.EtiquetaController import etiquetaController
from controllers.MovimientoController import movimientoController
import jsonpickle
from decimal import Decimal
from functions.DecimalHandler import DecimalHandler

################################################################
#Las siguientes 2 líneas son para que jsonpickle funcione con decimales ya que de lo contrario devolverá null en los JSON
jsonpickle.set_encoder_options('simplejson', use_decimal=True)
jsonpickle.handlers.registry.register(Decimal, DecimalHandler)
################################################################

#import mysql.connector
app = Flask(__name__)

# CORS(app)
CORS(app, resources={r"/cursos/*": {"origins": "http://localhost"}})
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

conexion=MySQL(app)

def convertJsonInObject(jsonDict):
    return namedtuple('X', jsonDict.keys())(*jsonDict.values())


def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.register_blueprint(usuarioController)
    app.register_blueprint(instrumentoController)
    app.register_blueprint(estatusController)
    app.register_blueprint(etiquetaController)
    app.register_blueprint(movimientoController)

    app.run(debug=True)