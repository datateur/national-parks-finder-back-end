from flask import Blueprint, request, jsonify, make_response, abort
import requests, os

parks_bp = Blueprint("parks", __name__, url_prefix="/parks")

@parks_bp.route('', method=["GET"])
def get_all_parks():
    