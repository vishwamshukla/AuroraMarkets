def parse_polygon_data(data):
    return [{'date': item['t'], 'price': item['c'], 'volume': item['v']} for item in data]