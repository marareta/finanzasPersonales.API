import json
from flask import Flask, jsonify
from flask_mysqldb import MySQL
from itsdangerous import JSONWebSignatureSerializer
import jsonpickle
from models.Instrumento import Instrumento
from models.InstrumentoValorDelDia import InstrumentoValorDelDia
from models.Error import Error
from models.ReporteGeneral import ReporteGeneral

app = Flask(__name__)
conexion=MySQL(app)

def ObtenerInstrumentosResumen():
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Instrumento_spSelInstrumentosResumenGeneral')
        datos = cursor.fetchall()
        cursor.close()
        retorno = []
        for fila in datos:
            obj = Instrumento()
            obj.instrumentoId = fila[0]
            obj.estatusId = fila[1]
            obj.estatus.estatusId = fila[1]
            obj.estatus.descripcion = fila[2]
            obj.descripcion = fila[3]
            obj.descripcionLarga = fila[4]
            obj.tipoInstrumentoId = fila[5]
            obj.tipoInstrumento.tipoInstrumentoId = fila[5]
            obj.tipoInstrumento.descripcion = fila[6]
            obj.tipoInstrumento.plataforma.plataformaId = fila[8]
            obj.tipoInstrumento.plataforma.descripcion = fila[9]
            obj.instrumentoPorcentajeObjetivo.porcentaje = fila[7]
            obj.saldo.monto = fila[10]
            obj.instrumentoPorcentajeReal.porcentaje = fila[11]
            obj.instrumentoFondoEmergencia.esFondoEmergencia = fila[12]
            obj.instrumentoColorBootstrap.colorBootstrapId = fila[13]
            obj.instrumentoColorBootstrap.colorBootstrap.colorBootstrapId = fila[13]
            obj.instrumentoColorBootstrap.colorBootstrap.descripcion = fila[14]
            obj.instrumentosValoresDelDia = ObtenerInstrumentroHistoriaValorDelDia(obj)
            retorno.append(obj)
        
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)


def ObtenerInstrumentroHistoriaValorDelDia(instrumento):
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Instrumento_spSelInstrumentosValorDelDiaHistoria', [instrumento.instrumentoId])
        datos = cursor.fetchall()
        cursor.close()
        retorno = []
        for fila in datos:
            obj = InstrumentoValorDelDia()
            obj.instrumentoId = instrumento.instrumentoId
            obj.valor = fila[1]
            obj.fecha = fila[2]
            obj.instrumento.instrumentoId = 0
            
            retorno.append(obj)
        
        return retorno
        
    except Exception as ex:
        return Error("Error", False, ex.args)


def ObtenerInstrumentosActivos():
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Instrumento_spSelInstrumentosActivos')
        datos = cursor.fetchall()
        cursor.close()
        retorno = []
        for fila in datos:
            obj = Instrumento()
            obj.instrumentoId = fila[0]
            obj.descripcion = fila[1]
            obj.descripcionLarga = fila[2]
            obj.tipoInstrumentoId = fila[3]
            obj.tipoInstrumento.tipoInstrumentoId = fila[3]
            obj.tipoInstrumento.descripcion = fila[4]
            obj.tipoInstrumento.plataforma.plataformaId = fila[5]
            obj.tipoInstrumento.plataforma.descripcion = fila[6]
            obj.instrumentoPorcentajeObjetivo.porcentaje = fila[7]
            obj.instrumentoFondoEmergencia.esFondoEmergencia = fila[8]
            obj.instrumentoColorBootstrap.colorBootstrapId = fila[9]
            obj.instrumentoColorBootstrap.colorBootstrap.colorBootstrapId = fila[9]
            obj.instrumentoColorBootstrap.colorBootstrap.descripcion = fila[10]
            obj.estatusId = fila[11]
            obj.estatus.estatusId = fila[11]
            obj.estatus.descripcion = fila[12]
            retorno.append(obj)
        
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)


def ObtenerInstrumentoInformacionGeneral(obj):
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Instrumento_spSelInstrumentoInformacionGeneral', [obj.instrumentoId])
        datos = cursor.fetchall()
        cursor.close()
        retorno = Instrumento()
        for fila in datos:
            retorno.instrumentoId = fila[0]
            retorno.descripcion = fila[1]
            retorno.descripcionLarga = fila[2]
            retorno.estatusId = fila[3]
            retorno.estatus.estatusId = fila[3]
            retorno.estatus.descripcion = fila[4]
            retorno.tipoInstrumentoId = fila[5]
            retorno.tipoInstrumento.tipoInstrumentoId = fila[5]
            retorno.tipoInstrumento.descripcion = fila[6]
            retorno.instrumentoFondoEmergencia.esFondoEmergencia = fila[7]
            retorno.saldo.monto = fila[8]
            retorno.instrumentoColorBootstrap.colorBootstrapId = fila[9]
            retorno.instrumentoColorBootstrap.colorBootstrap.colorBootstrapId = fila[9]
            retorno.instrumentoColorBootstrap.colorBootstrap.descripcion = fila[10]
        
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)


def ValidarInstrumentoExistenteValorDelDia(obj):
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Instrumento_spSelValidarInstrumentoExistenteValorDelDia', [obj.instrumentoValorDelDiaId, obj.instrumentoId, obj.fecha])
        datos = cursor.fetchall()
        cursor.close()
        retorno = InstrumentoValorDelDia()
        for fila in datos:
            retorno.instrumentoValorDelDiaId = fila[0]
            retorno.instrumentoId = fila[1]
            retorno.valor = fila[2]
            retorno.fecha = fila[3]
        
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)


def GuardarInstrumentoValorDelDia(obj):
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Instrumento_spInsInstrumentoValorDelDia', [obj.instrumentoValorDelDiaId, obj.instrumentoId, obj.fecha, obj.valor])
        datos = cursor.fetchall()
        cursor.close()
        retorno = InstrumentoValorDelDia()
        for fila in datos:
            retorno.instrumentoValorDelDiaId = fila[0]
            
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)


def ObtenerReporteGananciaPerdidaInversion():
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Instrumento_spSelInstrumentoValorDelDiaGananciaPerdida')
        datos = cursor.fetchall()
        cursor.close()
        retorno = ReporteGeneral()
        for fila in datos:
            retorno.montoTotal = fila[0]
            retorno.fecha = fila[1]
            retorno.porcentaje = fila[2]
        
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)