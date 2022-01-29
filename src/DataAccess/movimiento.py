from flask import Flask, jsonify
from flask_mysqldb import MySQL
from models.Movimiento import Movimiento

from models.ReporteGeneral import ReporteGeneral
from models.Error import Error
from models.MovimientoEtiqueta import MovimientoEtiqueta

app = Flask(__name__)
conexion=MySQL(app)

def ObtenerReporteGeneralDeInversiones():
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Movimientos_spSelMovimientosResumenGeneral')
        datos = cursor.fetchall()
        cursor.close()
        retorno = ReporteGeneral()
        obj = ReporteGeneral()
        for fila in datos:
            obj.fondoEmergencias = fila[0]
            obj.montoTotal = fila[1]
            obj.montoInvertido = fila[2]
        
        return (obj)
        
    except Exception as ex:
        return Error("Error", False, ex.args)


def ObtenerInversionPorEtiqueta():
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Movimientos_spSelInversionPorEtiqueta')
        datos = cursor.fetchall()
        cursor.close()
        retorno = []
        for fila in datos:
            reg = MovimientoEtiqueta()
            reg.etiquetaId = fila[0]
            reg.etiqueta.etiquetaId = fila[0]
            reg.etiqueta.descripcion = fila[1]
            reg.movimiento.monto = fila[2]
            retorno.append(reg)
        
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)


def GuardarMovimiento(obj, etiquetas):
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Movimientos_spInsMovimiento',[obj.movimientoId, obj.tipoMovimientoId, obj.fechaMovimiento, obj.instrumentoId, obj.monto, obj.esFondoEmergencias, etiquetas, obj.usuario.usuarioId, obj.comentarios, obj.cantidadAcciones])
        datos = cursor.fetchall()
        cursor.close()
        retorno = Movimiento()
        for fila in datos:
            retorno.movimientoId = fila[0]
        
        return (retorno)
        
    except Exception as ex:
        return Error("Error", False, ex.args)