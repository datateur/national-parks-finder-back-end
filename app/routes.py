from flask import Blueprint, request, jsonify, make_response, abort
from .data import get_all_national_parks_data
import requests, os

parks_bp = Blueprint("parks", __name__, url_prefix="/parks")
activities_bp = Blueprint("activities", __name__, url_prefix="/activities")
topics_bp = Blueprint("topics", __name__, url_prefix="/topics")

all_national_parks = get_all_national_parks_data()
NATIONAL_PARKS_SERVICE_API_KEY = os.environ['NATIONAL_PARKS_SERVICE_API_KEY']

# returns json object of all the parks
@parks_bp.route('', methods=["GET"])
def get_all_parks():
    return jsonify({'parks':all_national_parks}), 200


#returns json object of all the parks names and locations
@parks_bp.route('/locations', methods=["GET"])
def get_all_parks_location():
    all_parks_location = {}
    
    for park in all_national_parks:
        all_parks_location += {"park_id":park['parkCode'],
                                "park_name":park['fullName'], 
                                'location': {'lat': float(park['latitude']) if park['latitude'] else None, 'long': float(park['longitude']) if park['longitude'] else None}}

    return jsonify(all_parks_location)


@parks_bp.route('/filter', methods=["GET"])
def get_parks_filtered_by_activity():
    filter_activities = request.get_json()['activities']
    parks_by_activity = []

    for activity in filter_activities:
        for park in all_national_parks:
            for park_activity in park['activities']:
                if activity == park_activity['name']:
                    if park not in parks_by_activity:
                        parks_by_activity.append(park)


    print(len(parks_by_activity))
    return jsonify(parks_by_activity), 200


@activities_bp.route('', methods=["GET"])
def get_all_activities():
    activities = []
    response = requests.get("https://developer.nps.gov/api/v1/activities?",
                                    params={"api_key":NATIONAL_PARKS_SERVICE_API_KEY})
    
    for activity in response.json()['data']:
        activities.append(activity['name'])

    return jsonify({'activities':activities})


@topics_bp.route('', methods=["GET"])
def get_all_topics():
    topics = []
    response = requests.get("https://developer.nps.gov/api/v1/topics?",
                                    params={"api_key":NATIONAL_PARKS_SERVICE_API_KEY})
    
    for topic in response.json()['data']:
        topics.append(topic['name'])

    return jsonify({'topics':topics})




