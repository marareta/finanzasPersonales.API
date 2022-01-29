from flask import Flask, jsonify
from flask_mysqldb import MySQL

from models.TipoMovimiento import TipoMovimiento
from models.Error import Error

app = Flask(__name__)
conexion=MySQL(app)

def ObtenerTipoMovimientosActivos():
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Catalogo_spSelTipoMovimientosActivos')
        datos = cursor.fetchall()
        cursor.close()
        retorno = []
        for fila in datos:
            reg = TipoMovimiento()
            reg.tipoMovimientoId = fila[0]
            reg.descripcion = fila[1]
            retorno.append(reg)
        
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)