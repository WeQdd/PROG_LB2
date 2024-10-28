import requests
import json

def get_weather_data(place, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    
    result = {
        'name': data['name'],
        'coord': {'lon': data['coord']['lon'], 'lat': data['coord']['lat']},
        'country': data['sys']['country'],
        'feels_like': data['main']['feels_like'],
        'timezone': f'UTC{data["timezone"] // 3600:+}'
    }
    
    return result

