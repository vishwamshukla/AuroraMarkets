from flask import Blueprint, request, jsonify
from app.polygon_client import fetch_stock_data
from app.dynamodb_client import store_stock_data, query_stock_data, list_ticker_data

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/fetch-and-store', methods=['POST'])
def fetch_and_store():
    data = request.json
    ticker = data.get('ticker')
    date_range = data.get('date_range')

    if not ticker or not date_range:
        return jsonify({'error': 'Ticker and date_range are required'}), 400

    stock_data = fetch_stock_data(ticker, date_range)
    if not stock_data:
        return jsonify({'error': 'Failed to fetch data from Polygon.io'}), 500

    store_stock_data(ticker, stock_data)
    return jsonify({'message': 'Data fetched and stored successfully'}), 200

@api_blueprint.route('/query', methods=['GET'])
def query():
    ticker = request.args.get('ticker')
    date = request.args.get('date')

    if not ticker or not date:
        return jsonify({'error': 'Ticker and date are required'}), 400

    result = query_stock_data(ticker, date)
    if not result:
        return jsonify({'error': 'Data not found'}), 404

    return jsonify(result), 200

@api_blueprint.route('/list', methods=['GET'])
def list_data():
    ticker = request.args.get('ticker')

    if not ticker:
        return jsonify({'error': 'Ticker is required'}), 400

    result = list_ticker_data(ticker)
    return jsonify(result), 200