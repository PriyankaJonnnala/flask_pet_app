from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class PetForm(FlaskForm):
    name = StringField('Pet Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    type = StringField('Type of Pet', validators=[DataRequired()])
    submit = SubmitField('Add Pet')
