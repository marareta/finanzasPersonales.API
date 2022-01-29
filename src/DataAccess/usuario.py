from flask import Flask, jsonify
from flask_mysqldb import MySQL

from models.Usuario import Usuario
from models.UsuarioDatosGenerales import UsuarioDatosGenerales
from models.Error import Error

app = Flask(__name__)
conexion=MySQL(app)

def ValidaUsuarioLogin(usuario):
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Seguridad_spSelUsuarioLogin', [usuario.usuarioCredenciales.nombreUsuario, usuario.usuarioCredenciales.password])
        datos = cursor.fetchall()
        cursor.close()
        usuario = Usuario()
        for fila in datos:
            usuario.usuarioId = fila[0]
            usuario.estatusId = fila[1]
            usuario.estatus.estatusId = fila[1]
            usuario.estatus.descripcion = fila[2]
            
        if usuario.usuarioId != 0:
            usuario.usuarioDatosGenerales = ObtenerUsuarioDatosGenerales(usuario)

        return (usuario)
        
    except Exception as ex:
        return Error("Error", False, ex.args)


def ObtenerUsuarioDatosGenerales(usuario):
    try:
        cursor = conexion.connection.cursor()
        cursor.callproc('Seguridad_spSelUsuarioDatosGenerales', [usuario.usuarioId])
        datos = cursor.fetchall()
        cursor.close()
        retorno = UsuarioDatosGenerales()
        for fila in datos:
            retorno.nombres = fila[0]
            retorno.apellidoPaterno = fila[1]
            
        return retorno
        
    except Exception as ex:
        return Error("Error", False, ex.args)