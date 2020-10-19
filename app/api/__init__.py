from flask import Blueprint

api = Blueprint('api', __name__)

from app.api.query import query
from app.api.query import recent_info



