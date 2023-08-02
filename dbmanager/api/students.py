from flask import Blueprint, request, jsonify

from flask_cors import CORS
from dbmanager.api.utils import expect
from datetime import datetime


students_api_v1 = Blueprint(
    'students_api_v1', 'students_api_v1', url_prefix='/api/v1/students')

CORS(students_api_v1)


@students_api_v1.route('/', methods=['GET'])
def api_get_students():
    pass