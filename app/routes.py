from app import app
from flask import jsonify, request, json
import requests
import datetime

@app.route('/')
def weather():
    geo_api_key = '712ec370-4769-11ec-953a-1f6eeb0e6b17'
    geo_url = f'https://api.freegeoip.app/json?apikey={geo_api_key}'
    geo_request = requests.get(geo_url)
    geo_data = json.loads(geo_request.text)
    lat = geo_data["latitude"]
    lon = geo_data["longitude"]

    weather_api_key = "07d5d173fcf51ff7b9bebe64974490e8"
    weather_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={weather_api_key}&units=metric" 
    weather_response = requests.get(weather_url)
    weather_data = json.loads(weather_response.text)
    weather_results = {
        "datetime": datetime.datetime.fromtimestamp(weather_data["current"]["dt"]),
        "temperature": weather_data["current"]['temp'], 
        "timezone":  weather_data["timezone"],
        "humidity": weather_data["current"]['humidity'],
        "feels_like": weather_data["current"]['feels_like'],
        "wind_speed": weather_data["current"]['wind_speed'],
        "visibility": weather_data["current"]['visibility'],
        "pressure": weather_data["current"]['pressure'],
        "description": weather_data["current"]["weather"][0]["description"], 
        "icon": weather_data["current"]["weather"][0]["icon"],
        "icon_url": f"http://openweathermap.org/img/wn/{weather_data['current']['weather'][0]['icon']}@2x.png",
        "id": weather_data["current"]["weather"][0]["id"],
        "weather": weather_data["current"]["weather"][0]["main"]
        }

    return jsonify(weather_results)