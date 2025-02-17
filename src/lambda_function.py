import json
import random
import os

# API key que deberíamos obtener de una variable de entorno
VALID_API_KEY = os.environ.get('API_KEY', 'test-api-key-123')

# Coordenadas aproximadas de los continentes (para asegurar que caigan en tierra)
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
    # Selecciona un continente al azar
    continent = random.choice(CONTINENT_BOUNDS)
    
    # Genera coordenadas aleatorias dentro del continente
    latitude = random.uniform(continent['min_lat'], continent['max_lat'])
    longitude = random.uniform(continent['min_lon'], continent['max_lon'])
    
    return round(latitude, 6), round(longitude, 6)

def lambda_handler(event, context):
    # Obtener query parameters
    query_params = event.get('queryStringParameters', {}) or {}
    api_key = query_params.get('api_key')
    ip = query_params.get('ip')
    
    # Validar API key
    if not api_key or api_key != VALID_API_KEY:
        return {
            'statusCode': 401,
            'body': json.dumps({'error': 'Invalid API key'})
        }
    
    # Validar IP
    if not ip:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'IP parameter is required'})
        }
    
    # Generar coordenadas aleatorias
    latitude, longitude = get_random_coordinates()
    
    # Preparar respuesta
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
