from flask import Flask, jsonify
from flask_mysqldb import MySQL

from models.Etiqueta import Etiqueta
from models.Error import Error

app = Flask(__name__)
conexion=MySQL(app)

def ObtenerEtiquetasActivas():
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Catalogo_spSelEtiquetasActivas')
        datos = cursor.fetchall()
        cursor.close()
        retorno = []
        for fila in datos:
            reg = Etiqueta()
            reg.etiquetaId = fila[0]
            reg.descripcion = fila[1]
            retorno.append(reg)
        
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)

def ObtenerEtiquetas():
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Catalogo_spSelEtiquetas')
        datos = cursor.fetchall()
        cursor.close()
        retorno = []
        for fila in datos:
            reg = Etiqueta()
            reg.etiquetaId = fila[0]
            reg.descripcion = fila[1]
            retorno.append(reg)
        
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)


def ObtenerEtiquetaPorId(obj):
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Catalogo_spSelEtiquetaPorId',[obj.etiquetaId])
        datos = cursor.fetchall()
        cursor.close()
        retorno = Etiqueta()
        for fila in datos:
            retorno.etiquetaId = fila[0]
            retorno.descripcion = fila[1]
            retorno.estatus.descripcion = fila[2]
            retorno.estatusId = fila[3]
            retorno.estatus.estatusId = fila[3]
        
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)


def ValidarEtiqueta(obj):
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Catalogo_spSelValidaEtiqueta',[obj.etiquetaId, obj.descripcion])
        datos = cursor.fetchall()
        cursor.close()
        retorno = ''
        for fila in datos:
            retorno = fila[0]
            
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)


def GuardarEiqueta(obj):
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Catalogo_spInsEtiqueta',[obj.etiquetaId, obj.descripcion, obj.estatusId])
        datos = cursor.fetchall()
        cursor.close()
        retorno = Etiqueta()
        for fila in datos:
            retorno.etiquetaId = fila[0]
        
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)


