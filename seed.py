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
            type = park['designation'],
            images = [{'url': image['url'], 'caption': image['caption'],
                        'title': image['title'], 'altText': image['altText']} 
                        for image in park['images']],
            fees = [{'cost': fee['cost'], 'description': fee['description'],
                    'title': fee['title']} for fee in park['entranceFees']],
            operating_hours = [{'name': site['name'], 'standardHours': site['standardHours'],
                                'description': site['description']} for site in park['operatingHours']],
            addresses = [{'line1': address['line1'], 'line2': address['line2'], 'line3': address['line3'],
                        'city': address['city'], 'state': address['stateCode'], 'postalCode': address['postalCode']}
                        for address in park['addresses'] if address['type'] == 'Physical']
        )

        list_of_parks_to_add_to_db.append(park_to_add)

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