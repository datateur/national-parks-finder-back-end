from flask import Blueprint, request, jsonify#, make_response, abort
import requests, os
from app.models.park import Park
from sqlalchemy.dialects.postgresql import ARRAY
from app import db

parks_bp = Blueprint("parks", __name__, url_prefix="/parks")
activities_bp = Blueprint("activities", __name__, url_prefix="/activities")
topics_bp = Blueprint("topics", __name__, url_prefix="/topics")
types_bp = Blueprint("types", __name__, url_prefix="/types")

NATIONAL_PARKS_SERVICE_API_KEY = os.environ['NATIONAL_PARKS_SERVICE_API_KEY']

@parks_bp.route('/filter', methods=["POST"])
def get_filtered_parks():
    filter_activities = request.get_json()['activities']
    filter_topics = request.get_json()['topics']
    filter_types = request.get_json()['types']

    query = Park.query
    response = []
        
    if filter_activities:
        query = query.filter(Park.activities.contains(db.cast(filter_activities, ARRAY(db.String))))

    if filter_topics:
        query = query.filter(Park.topics.contains(db.cast(filter_topics, ARRAY(db.String))))
    
    if filter_types:
        query = query.filter(Park.type.in_(filter_types))

    filtered_parks = query.all()

    for park in filtered_parks:
        response.append(park.to_dict())

    return jsonify(response), 200


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


@types_bp.route('', methods=["GET"])
def get_all_park_types():
    types = []

    parks = Park.query.all()

    for park in parks:
        if park.__dict__['designation'] and park.__dict__['designation'] not in types:
            types.append(park.__dict__['designation'])
    
    return jsonify({'types': types}), 200








