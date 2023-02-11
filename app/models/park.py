from app import db
from sqlalchemy.dialects.postgresql import ARRAY

class Park(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String)
    full_name = db.Column(db.String)
    park_code = db.Column(db.String)
    description = db.Column(db.Text)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    activities = db.Column(ARRAY(db.String))
    topics = db.Column(ARRAY(db.String))
    states = db.Column(db.String)
    phone_numbers = db.Column(db.ARRAY(db.JSON))
    emails = db.Column(db.ARRAY(db.String))
    fees = db.Column(db.ARRAY(db.JSON))
    operating_hours = db.Column(db.ARRAY(db.JSON))
    images = db.Column(db.ARRAY(db.JSON))
    designation = db.Column(db.String)
    addresses = db.Column(db.ARRAY(db.JSON))


    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'fullName': self.full_name,
            'parkCode': self.park_code,
            'description': self.description,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'activities': self.activities,
            'topics': self.topics,
            'states': self.states,
            'phoneNumbers': self.phone_numbers,
            'emails': self.emails,
            'fees': self.fees,
            'operatingHours': self.operating_hours,
            'images': self.images,
            'designation': self.designation,
            'addresses': self.addresses
        }




