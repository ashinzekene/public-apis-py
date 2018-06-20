"""Sample API routes."""
from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.utils.scrap import scrap
from os import getenv

api_bp = Blueprint('api', __name__)


@api_bp.route('/', methods=['GET'])
def home():
    """Welcome page/message."""
    return jsonify({'message': 'Hello World!'})


@api_bp.route('/journal', methods=['GET'])
def journal():
    """Welcome page/message."""
    journal_id = request.args.get('doi', '')
    api_url = getenv("API_URL") + journal_id
    url = scrap(api_url, "iframe", False)
    return jsonify({'url': url})


@api_bp.route('/protected', methods=['GET'])
@login_required
def protected():
    """A protected route."""
    return jsonify({'message': 'You are logged-in.'})
