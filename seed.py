"""Seed pets db with data"""

from app import app
from models import db, Pet

app.app_context().push()

db.drop_all()
db.create_all()

joe_furrow = Pet(
    name="Joe Furrow",
    species="English Long Hair",
    age="baby",
    notes="",
    available=True,
    photo_url="https://www.dailypaws.com/thmb/qAkdPQG4mKmYYTG4QHtyxUY-Dgo=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/british-longhaired-kitten-107842351-2000-d3b39dfd9db241b09b32ff041a0f0b77.jpg"
)

patrick_meowhomes = Pet(
    name="Patrick Meowhomes",
    species="Siamese",
    age="young",
    notes="",
    available=False,
    photo_url="https://preview.redd.it/955h4hhrz2781.jpg?width=640&crop=smart&auto=webp&s=26c0a181384047a6908688b506b9599b2bd4a6b2"
)

db.session.add_all([joe_furrow, patrick_meowhomes])
db.session.commit()
