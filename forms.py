from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField


class AddWordForm(FlaskForm):
    statement = StringField(label='Wpisz slowo')
    submit = SubmitField(label='Add word or hit enter')