import requests, os
import pprint

NATIONAL_PARKS_SERVICE_API_KEY = os.environ.get("NATIONAL_PARKS_SERVICE_API_KEY")

response = requests.get("https://developer.nps.gov/api/v1/parks?", params={"api_key":NATIONAL_PARKS_SERVICE_API_KEY, "limit": 1})
pprint.pprint(response.json()["data"][0])