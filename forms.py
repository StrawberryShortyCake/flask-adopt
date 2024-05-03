from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, URL

"""Forms for adopt app."""


class AddPetForm(FlaskForm):
    """Form for adding pet"""

    name = StringField(
        "Pet Name:",
        validators=[InputRequired()])
    species = StringField(
        'Species:',
        validators=[InputRequired()]
    )
    photo_url = StringField(
        'Photo URL:',
        validators=[URL()])
    age = SelectField(
        'Age:',
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')
        ],
        validators=[InputRequired()])
    notes = StringField('Notes:')
