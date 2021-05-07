from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired




class TaskForm(FlaskForm):
    desc = StringField('Description of Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')
