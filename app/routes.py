from flask import Blueprint, request, jsonify, make_response, abort
from .data import get_all_national_parks_data
import requests, os

parks_bp = Blueprint("parks", __name__, url_prefix="/parks")

all_national_parks = get_all_national_parks_data()

# returns json object of all the parks
@parks_bp.route('', methods=["GET"])
def get_all_parks():
    
    return jsonify({'parks':all_national_parks})

# # returns json object of all the parks locations
# @parks_bp.route('', method=["GET"])
# def get_all_parks_lat_long():
#     all_parks_lat_long = []
#     for park in all_national_parks:

#     return jsonify()