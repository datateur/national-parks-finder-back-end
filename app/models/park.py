from app import db
from sqlalchemy.dialects.postgresql import ARRAY
# using this with Park.query.filter(Park.activities.contains(filter_activities)) in tiler route
# is the same as using Park.query.filter(Park.activities.op("@>")(filter_activities)) without import

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
    #fees = db.Column(db.ARRAY(db.))
    #operating_hours = db.Column
    #images = db.Column
    designation = db.Column(db.String)



    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'full_name': self.full_name,
            'park_code': self.park_code,
            'description': self.description,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'activities': self.activities,
            'topics': self.topics,
            'states': self.states,
            'phone_numbers': self.phone_numbers,
            'emails': self.emails,
            'designation': self.designation
        }




