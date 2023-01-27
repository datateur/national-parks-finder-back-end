from flask import Blueprint, request, jsonify, make_response, abort
from .data import get_all_national_parks_data
import requests, os

parks_bp = Blueprint("parks", __name__, url_prefix="/parks")

all_national_parks = get_all_national_parks_data()

# # returns json object of all the parks
# @parks_bp.route('', methods=["GET"])
# def get_all_parks():
#     return jsonify({'parks':all_national_parks})

# returns json object of all the parks locations
@parks_bp.route('', methods=["GET"])
def get_all_parks_location():
    all_parks_location = []
    
    for park in all_national_parks:
        all_parks_location.append({"park_name":park['fullName'], 'location':park['latLong']})

    return jsonify(all_parks_location)