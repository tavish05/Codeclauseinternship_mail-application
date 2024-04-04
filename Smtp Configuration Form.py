from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SMTPForm(FlaskForm):
    host = StringField('SMTP Host')
    port = StringField('SMTP Port')
    username = StringField('SMTP Username')
    password = PasswordField('SMTP Password')
    submit = SubmitField('Save Settings')
