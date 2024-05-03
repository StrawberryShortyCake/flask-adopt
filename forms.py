from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

"""Forms for adopt app."""


class AddPetForm(FlaskForm):
    """Form for adding pet"""

    name = StringField("Pet Name:")
    species = StringField('Species:')
    photo_url = StringField('Photo URL:')
    age = StringField('Age:')
