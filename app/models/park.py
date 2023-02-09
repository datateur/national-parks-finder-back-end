from app import db

class Park(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String)
    full_name = db.Column(db.String)
    park_code = db.Column(db.String)
    description = db.Column(db.Text)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    activities = db.Column(db.ARRAY(db.String))
    topics = db.Column(db.ARRAY(db.String))
    states = db.Column(db.String)
    phone_numbers = db.Column(db.ARRAY(db.JSON))
    emails = db.Column(db.ARRAY(db.String))



