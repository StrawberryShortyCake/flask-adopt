"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, flash, request
from flask_debugtoolbar import DebugToolbarExtension

from models import db, dbx, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['SECRET_KEY'] = "secret"
db.init_app(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def display_pets():

    q_pets = db.select(Pet).order_by(Pet.name)
    pets = dbx(q_pets).scalars().all()

    return render_template('homepage.jinja', pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """"form for adding pets; handle adding"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f'{new_pet.name} has been added to the list!')
        return redirect("/")

    else:
        return render_template("form.jinja", form=form)
