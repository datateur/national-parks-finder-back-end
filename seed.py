from app import create_app, db
from app.models.park import Park
from app.data import get_all_national_parks_data
import json

def getParks():
    all_parks = get_all_national_parks_data()
    list_of_parks_to_add_to_db = []
    for park in all_parks:
        park_to_add = Park(
            url = park['url'],
            full_name = park['fullName'],
            description = park['description'],
            latitude = float(park['latitude']) if park['latitude'] else None,
            longitude = float(park['longitude']) if park['longitude'] else None,
            states = park['states'],
            activities = [activity['name'] for activity in park['activities']],
            topics = [topic['name'] for topic in park['topics']],
            park_code = park['parkCode'],
            phone_numbers = [{'phoneNumber': number['phoneNumber'],
                                        'type': number['type']} 
                                        for number in park['contacts']['phoneNumbers']],
            emails = [email['emailAddress'] for email in park['contacts']['emailAddresses']],
            designation = park['designation']
        )

        # if fountain_to_add.type == '':
        #     fountain_to_add.type = 'PUBLIC DRINKING FOUNTAIN'
        list_of_parks_to_add_to_db.append(park_to_add)

        # if fountain_to_add.borough == 'M':
        #     fountain_to_add.borough = 'Manhattan'
        # if fountain_to_add.borough == 'B':
        #     fountain_to_add.borough = 'Brooklyn'
        # if fountain_to_add.borough == 'X':
        #     fountain_to_add.borough = 'Bronx'
        # if fountain_to_add.borough == 'Q':
        #     fountain_to_add.borough = 'Queens'
        # if fountain_to_add.borough == 'R':
        #     fountain_to_add.borough = 'Staten Island'

    return list_of_parks_to_add_to_db


def load():
    app = create_app()

    parks = getParks()

    with app.app_context():
        db.session.add_all(parks)
        db.session.commit()


def main():
    load()


if __name__ == "__main__":
    main()