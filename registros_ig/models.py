import sqlite3
from registros_ig import ORIGIN_DATA
from registros_ig.conexion import Conexion

def select_all():

    conectar = Conexion('select * from movements order by date desc;')
    filas = conectar.res.fetchall() #datos de columnas (1,2024-01-01,nomina enero, 1500)
    columnas = conectar.res.description #nombres de columnas (id,00000)(date,00000)(concept,00000)
    
    lista_diccionario = []
    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion +=1
        lista_diccionario.append(diccionario)
    conectar.con.close()

    return lista_diccionario

def insert(registroForm):
    conectarInser = Conexion('insert into movements (date,concept,quantity) values(?,?,?);',registroForm)
    conectarInser.con.commit()#Funcion para validar registro
    conectarInser.con.close()

def select_by(id):
    conectarSelectBy = Conexion(f'select * from movements where id={id};')
    result = conectarSelectBy.res.fetchall()
    conectarSelectBy.con.close()

    return result[0]

def delete_by(id):
    conectarDeleteBy = Conexion(f'delete from movements where id={id};')
    conectarDeleteBy.con.commit() #funcion para validar borrado
    conectarDeleteBy.con.close() 

def update_by(id,registro):
    conectUpdate = Conexion(f'update movements set date=?, concept=? , quantity=? WHERE id={id}',registro)
    conectUpdate.con.commit()
    conectUpdate.con.close()

def select_ingreso():
    conectIngreso = Conexion('select sum(quantity) from movements where quantity >0;')
    resultadoIngreso = conectIngreso.res.fetchall()
    conectIngreso.con.close()

    return resultadoIngreso[0][0]

def select_egreso():
    conectEgreso = Conexion('select sum(quantity) from movements where quantity <0;')
    resultadoEgreso = conectEgreso.res.fetchall()
    conectEgreso.con.close()

    return resultadoEgreso[0][0]