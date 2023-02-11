from flask import Blueprint, request, jsonify, make_response, abort
import requests, os
from app.models.park import Park
from sqlalchemy.dialects.postgresql import ARRAY
from app import db

parks_bp = Blueprint("parks", __name__, url_prefix="/parks")
activities_bp = Blueprint("activities", __name__, url_prefix="/activities")
topics_bp = Blueprint("topics", __name__, url_prefix="/topics")

NATIONAL_PARKS_SERVICE_API_KEY = os.environ['NATIONAL_PARKS_SERVICE_API_KEY']

# returns json object of all the parks
# @parks_bp.route('', methods=["GET"])
# def get_all_parks():
#     parks = Park.query.all()
#     response = []
#     for park in parks:
#         response.append(park.to_dict())
    
#     return jsonify(response), 200


# @parks_bp.route('/filter', methods=["POST"])
# def get_parks_filtered_by_activity_and_topic():
#     filter_activities = request.get_json()['activities']
#     filter_topics = request.get_json()['topics']
#     parks_by_activity = []
#     parks_by_topic = []
#     filtered_parks = []

#     if not filter_activities and not filter_topics:
#         for park in all_national_parks:
#             filtered_parks.append({"park_id":park['parkCode'],
#                                     "full_name":park['fullName'], 
#                                     'description': park['description'],
#                                     'latitude': float(park['latitude']) if park['latitude'] else None,
#                                     'longitude': float(park['longitude']) if park['longitude'] else None,
#                                     'states': [park['states']],
#                                     'contacts': [park['contacts']],
#                                     'entranceFees': [park['entranceFees']],
#                                     'hours': park['operatingHours'],
#                                     'designation': park['designation']})
        
#     else:
#         for park in all_national_parks:
#             if filter_activities:
#                 for activity in filter_activities:
#                     for park_activity in park['activities']:
#                         if activity == park_activity['name'] and park not in parks_by_activity:
#                             parks_by_activity.append({"park_id":park['parkCode'],
#                                     "full_name":park['fullName'],
#                                     'description': park['description'],
#                                     'latitude': float(park['latitude']) if park['latitude'] else None,
#                                     'longitude': float(park['longitude']) if park['longitude'] else None,
#                                     'states': [park['states']],
#                                     'contacts': [park['contacts']],
#                                     'entranceFees': [park['entranceFees']],
#                                     'hours': park['operatingHours'],
#                                     'designation': park['designation']})
            
#             if filter_topics:
#                 for topic in filter_topics:
#                     for park_topic in park['topics']:
#                         if topic == park_topic['name'] and park not in parks_by_topic:
#                             parks_by_topic.append({"park_id":park['parkCode'],
#                                     "full_name": park['fullName'],
#                                     'description': park['description'],
#                                     'latitude': float(park['latitude']) if park['latitude'] else None,
#                                     'longitude': float(park['longitude']) if park['longitude'] else None,
#                                     'states': [park['states']],
#                                     'contacts': [park['contacts']],
#                                     'entranceFees': [park['entranceFees']],
#                                     'hours': park['operatingHours'],
#                                     'designation': park['designation']})
    
#         if parks_by_activity and parks_by_topic:
#             filtered_parks = [park for park in parks_by_activity if park in parks_by_topic]
#         else:
#             filtered_parks = parks_by_activity + parks_by_topic

#     return jsonify(filtered_parks), 200

@parks_bp.route('/filter/db', methods=["POST"])
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







