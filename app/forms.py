from flask.ext.wtf import Form, RecaptchaField
from wtforms import StringField
from wtforms.fields.html5 import EmailField, URLField
from wtforms.validators import Required, Email, URL, Length

class AddGame(Form):
    title = StringField('Title*', validators=[Required(), Length(max=30)])
    mail = EmailField('Your email*', validators=[Required(), Email(), Length(max=60)])
    link = URLField('Game URL*', validators=[Required(), URL(), Length(max=30)])
    desc = StringField('Description', validators=[Length(max=300)])
    #capt = RecaptchaField()
