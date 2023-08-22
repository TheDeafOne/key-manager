from flask import Blueprint, request, jsonify

from flask_cors import CORS
from dbmanager.api.utils import expect
from datetime import datetime
from dbmanager.db import get_students

students_api_v1 = Blueprint(
    'students_api_v1', 'students_api_v1', url_prefix='/api/v1/students')

CORS(students_api_v1)


@students_api_v1.route('/', methods=['GET'])
def api_get_students():
    return jsonify(get_students(None))
    