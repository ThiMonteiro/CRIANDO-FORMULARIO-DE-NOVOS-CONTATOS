from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class Info(FlaskForm):
    nome = StringField(label="Nome: ", validators=[Length(min=2, max=30), DataRequired()])
    sobrenome = StringField(label="Sobrenome: ", validators=[Length(min=2, max=30), DataRequired()])
    apelido = StringField(label="Apelido: ", validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label="Email: ", validators=[Email(), DataRequired()])
    salvar = SubmitField(label="Salvar contato")
    