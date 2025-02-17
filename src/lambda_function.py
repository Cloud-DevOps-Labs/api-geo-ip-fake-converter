import json
import random
import os
import ipaddress

def is_valid_ip(ip_string):
    try:
        ipaddress.ip_address(ip_string)
        return True
    except ValueError:
        return False

# API key that should be obtained from an environment variable
VALID_API_KEY = os.environ.get('API_KEY', 'test-api-key-123')

# Approximate coordinates of continents (to ensure coordinates fall on land)
CONTINENT_BOUNDS = [
    # Norte América
    {'min_lat': 25, 'max_lat': 70, 'min_lon': -165, 'max_lon': -50},
    # Sur América
    {'min_lat': -55, 'max_lat': 12, 'min_lon': -80, 'max_lon': -35},
    # Europa
    {'min_lat': 35, 'max_lat': 70, 'min_lon': -10, 'max_lon': 40},
    # África
    {'min_lat': -35, 'max_lat': 35, 'min_lon': -20, 'max_lon': 50},
    # Asia
    {'min_lat': 0, 'max_lat': 75, 'min_lon': 45, 'max_lon': 180},
]

def get_random_coordinates():
    # Select a random continent
    continent = random.choice(CONTINENT_BOUNDS)
    
    # Generate random coordinates within the continent
    latitude = random.uniform(continent['min_lat'], continent['max_lat'])
    longitude = random.uniform(continent['min_lon'], continent['max_lon'])
    
    return round(latitude, 6), round(longitude, 6)

def lambda_handler(event, context):
    # Get query parameters
    query_params = event.get('queryStringParameters', {}) or {}
    api_key = query_params.get('api_key')
    ip = query_params.get('ip')
    
    # Validate API key
    if not api_key or api_key != VALID_API_KEY:
        return {
            'statusCode': 401,
            'body': json.dumps({'error': 'Invalid API key'})
        }
    
    # Validate IP presence
    if not ip:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'IP parameter is required'})
        }

    # Validate IP format
    if not is_valid_ip(ip):
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid IP format'})
        }
    
    # Generate random coordinates
    latitude, longitude = get_random_coordinates()
    
    # Prepare response
    response = {
        'ip': ip,
        'latitude': latitude,
        'longitude': longitude
    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response)
    }
