# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Title', validators= [DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    poster = FileField('Poster', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add Movie Poster')