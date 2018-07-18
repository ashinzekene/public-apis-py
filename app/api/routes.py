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
    api_url = getenv("JOURNAL_API_URL2") + journal_id
    print(api_url)
    urls = scrap_url(api_url, ".search-results-list__item-title a", "href")
    if urls == "Not Found" or len(urls) == 0:
        return jsonify({'urls': []})
        # print("""
        # --------------------------------------
        #            Not Found
        # --------------------------------------
        # """)
        # api_url = getenv("JOURNAL_API_URL2") + journal_id
        # urls = scrap_url(api_url, ".search-results-list__item-title a", "href")
        # if urls == "Not Found":
        #     print('Not found on the second url')
        #     return jsonify({'url': urls })
        # else:
        # to_url = lambda x : getenv("JOURNAL_DOWNLOAD_API_URL2") + x.replace("/item/detail/id/", "")
        # download_urls = list(map(to_url, urls))
    else:
        for x in urls:
            print(x)
            x['url'] = getenv("JOURNAL_DOWNLOAD_API_URL2") + x['url'].replace("/item/detail/id/", "")
        return jsonify({'urls': urls})


@api_bp.route('/protected', methods=['GET'])
@login_required
def protected():
    """A protected route."""
    return jsonify({'message': 'You are logged-in.'})
