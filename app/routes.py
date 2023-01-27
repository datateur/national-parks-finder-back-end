from flask import Blueprint, request, jsonify, make_response, abort
from .data import get_all_national_parks_data
import requests, os

parks_bp = Blueprint("parks", __name__, url_prefix="/parks")

all_national_parks = get_all_national_parks_data()

# returns json object of all the parks
@parks_bp.route('', methods=["GET"])
def get_all_parks():
    return jsonify({'parks':all_national_parks}), 200


# returns json object of all the parks names and locations
# @parks_bp.route('', methods=["GET"])
# def get_all_parks_location():
#     all_parks_location = []
    
#     for park in all_national_parks:
#         all_parks_location.append({"park_name":park['fullName'], 'location':park['latLong']})

#     return jsonify(all_parks_location)


@parks_bp.route('/activity', methods=["GET"])
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


