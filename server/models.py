from flask_sqlalchemy import SQLAlchemy

# Create the db instance (to be initialized in app.py)
db = SQLAlchemy()

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Pet {self.id} {self.name} ({self.species})>'
