from registros_ig import app
from flask import render_template, request, redirect
from registros_ig.models import *
from datetime import date

def validarFormulario(datosFormulario):
    errores = []
    hoy  = str(date.today())
    if datosFormulario['date'] > hoy:
        errores.append('La fecha no puede ser mayor a la actual')
    if datosFormulario['concept'] == '':
        errores.append('El concepto no puede ir vacio')
    if datosFormulario['quantity'] == '' or float(datosFormulario['quantity']) == 0.0:
        errores.append('El monto debe ser distinto de 0 y de vacio')
    
    return errores

@app.route('/')
def index():
    dic = select_all()
    return render_template('index.html',datos = dic)

@app.route('/new',methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html', dataForm = {})
    else:
        errores = validarFormulario(request.form)
        if errores:
            return render_template('create.html',errors = errores,dataForm=request.form)
        
        insert((request.form['date'],request.form['concept'],request.form['quantity']))
        return redirect('/') 

@app.route('/delete/<int:id>',methods=['GET','POST'])
def remove(id):
    if request.method == 'GET':
        resultado = select_by(id)
        return render_template('delete.html',data=resultado)
    else:
        return 'Registro para eliminar'