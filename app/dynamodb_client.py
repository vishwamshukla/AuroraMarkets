import boto3
import os

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table_name = os.getenv('DYNAMODB_TABLE_NAME')
table = dynamodb.Table(table_name)

def store_stock_data(ticker, stock_data):
    for record in stock_data:
        table.put_item(
            Item={
                'ticker': ticker,
                'date': record['t'],  # Timestamp
                'price': record['c'],  # Closing price
                'volume': record['v']  # Volume
            }
        )

def query_stock_data(ticker, date):
    response = table.get_item(
        Key={
            'ticker': ticker,
            'date': date
        }
    )
    return response.get('Item')

def list_ticker_data(ticker):
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('ticker').eq(ticker)
    )
    return response.get('Items', [])