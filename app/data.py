import requests, os

#returns a list holding dicts of all the national parks
def get_all_national_parks_data():
    national_parks = []
    NATIONAL_PARKS_SERVICE_API_KEY = os.environ['NATIONAL_PARKS_SERVICE_API_KEY']
    
    # makes 10 api calls to get all 468 parks (request limit is 50)
    start_int = 0
    while start_int <= 500:
            response = requests.get("https://developer.nps.gov/api/v1/parks?",
                                    params={"api_key":NATIONAL_PARKS_SERVICE_API_KEY, "start":start_int})

            if response.status_code == 200:
                national_parks += response.json()['data']
                start_int += 50
            
            else:
                print(response.status_code, '/n', response.text)
                break

            # patch to add missing lat and lon data to site
            for park in national_parks:
                if park['fullName'] == 'Blackwell School National Historic Site':
                    park['latitude'] = '30.305819'
                    park['longitude'] = '-104.022421'
                    park['latLong'] = "lat: 30.305819, long:-104.022421"

    
    print(len(national_parks))
    return national_parks



