from flask import Blueprint, request, jsonify, make_response, abort
import requests, os
from app.models.park import Park
from sqlalchemy.dialects.postgresql import ARRAY
from app import db

parks_bp = Blueprint("parks", __name__, url_prefix="/parks")
activities_bp = Blueprint("activities", __name__, url_prefix="/activities")
topics_bp = Blueprint("topics", __name__, url_prefix="/topics")

NATIONAL_PARKS_SERVICE_API_KEY = os.environ['NATIONAL_PARKS_SERVICE_API_KEY']

@parks_bp.route('/filter', methods=["POST"])
def get_parks_filtered_db():
    filter_activities = request.get_json()['activities']
    filter_topics = request.get_json()['topics']
    filtered_parks = []
    response = []
        
    if filter_activities and filter_topics:
        filtered_parks = Park.query.filter(Park.activities.contains(db.cast(filter_activities, ARRAY(db.String))), Park.topics.contains(db.cast(filter_topics, ARRAY(db.String)))).all()

    elif filter_activities:
        filtered_parks = Park.query.filter(Park.activities.contains(db.cast(filter_activities, ARRAY(db.String)))).all()
    
    elif filter_topics:
        filtered_parks = Park.query.filter(Park.topics.contains(db.cast(filter_topics, ARRAY(db.String)))).all()
    
    else:
        filtered_parks = Park.query.all()


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







