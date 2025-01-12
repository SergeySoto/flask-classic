from flask_wtf import FlaskForm
from wtforms import DateField,StringField,FloatField,SubmitField
from wtforms.validators import DataRequired,length,ValidationError
from datetime import date

class MovementsForm(FlaskForm):
    date = DateField('Fecha',validators=[ DataRequired(message='La fecha es requerida') ])
    concept = StringField('Concepto', validators=[ DataRequired(message='El concepto es requerido'),length(min=4,message='Mas de 4 caracteres por favor')])
    quantity = FloatField('Monto',validators=[ DataRequired(message='El monto es requerido') ])
    
    submit= SubmitField('Guardar')

def validate_date(form,field):
    if field.data > date.today():
        raise ValidationError('Fecha invalidad: La fecha no debe ser mayor a hoy')