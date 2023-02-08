from app import db

class Park(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String)
    full_name = db.Column(db.String)
    park_code = db.Column(db.String)
    description = db.Column(db.Text)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    activities = db.Column(db.Array(db.json)) # ???
    topics = db.Column(db.Array(db.json)) # ???
    states = db.Column(db.String)



