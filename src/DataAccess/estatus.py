from flask import Flask, jsonify
from flask_mysqldb import MySQL

from models.Estatus import Estatus
from models.TipoObjeto import TipoObjeto
from models.Error import Error

app = Flask(__name__)
conexion=MySQL(app)

def ObtenerEstatusPorTipoObjeto(obj):
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Catalogo_spSelEstatusPorTipoDeObjeto', [obj.descripcion])
        datos = cursor.fetchall()
        cursor.close()
        retorno = []
        for fila in datos:
            reg = Estatus()
            reg.estatusId = fila[0]
            reg.descripcion = fila[1]
            retorno.append(reg)
        
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)