import sqlite3

def select_all():
    conexion = sqlite3.connect("data/db_movimientos.sqlite")
    cur = conexion.cursor()
    res = cur.execute('SELECT * from movements;')
    filas = res.fetchall() #datos de columnas (1,2024-01-01,nomina enero, 1500)
    columnas = res.description #nombres de columnas (id,00000)(date,00000)(concept,00000)
    
    lista_diccionario = []
    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion +=1
        lista_diccionario.append(diccionario)
    conexion.close()

    return lista_diccionario

def insert(registroForm):
    conexion = sqlite3.connect('data/db_movimientos.sqlite')
    cur = conexion.cursor()
    res = cur.execute('insert into movements (date,concept,quantity) values(?,?,?);',registroForm)

    conexion.commit()#Funcion para validar registro

    conexion.close()