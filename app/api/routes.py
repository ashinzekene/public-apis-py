"""Sample API routes."""
from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.utils.scrap import scrap, fetch_url_text, scrap_url
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
    api_url = getenv("JOURNAL_API_URL1") + journal_id
    url = scrap_url(api_url, "iframe", "src")
    if url == "Not Found":
        print("""
        --------------------------------------
        Not Found: Using the second crawl site
        --------------------------------------
        """)
        api_url = getenv("JOURNAL_API_URL2") + journal_id
        url = scrap_url(api_url, ".search-results-list__item-title a", "href")
        if url == "Not Found":
            print('Not found on the second url')
            return jsonify({'url': url })
        else:
            download_url = getenv("JOURNAL_DOWNLOAD_API_URL2") + url.replace("/item/detail/id/", "")
            return jsonify({'url': download_url })
    else:
        return jsonify({'url': url})


@api_bp.route('/protected', methods=['GET'])
@login_required
def protected():
    """A protected route."""
    return jsonify({'message': 'You are logged-in.'})
