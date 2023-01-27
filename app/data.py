import requests, os
import pprint

#returns a list holding json objects of all the national parks. 
def get_all_national_parks_data():
    national_parks = []
    NATIONAL_PARKS_SERVICE_API_KEY = os.environ['NATIONAL_PARKS_SERVICE_API_KEY']
    
    # make 10 api calls to get all 468 parks (limit for each request is 50)
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

    return national_parks

#pprint.pprint(get_all_national_parks_data()[0]['fullName'])


