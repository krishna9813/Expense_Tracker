import requests
from flask import Flask, request, session, g, abort, render_template, redirect, url_for, flash
import json
app = Flask(__name__)
@app.route('/')
def fetch_weather(city):
    params = {
        "q": city,
        "appid": "431fe6a6010d45baa56155000240702" 
    }
    WEATHER_API_URL = "https://www.weatherapi.com/"
    response = requests.get(WEATHER_API_URL, params=params)
    try:
        weather_data = response.json()
        return weather_data
    except json.decoder.JSONDecodeError:
        print("Error: Unable to decode JSON response from the weather API")
        return None

def weather():
    city = request.args.get('city', 'New York') 
    weather_data = fetch_weather(city)
    if weather_data:
        temperature = weather_data.get('main', {}).get('temp')
        description = weather_data.get('weather', [{}])[0].get('description')
        return render_template('login.html', temperature=temperature, description=description, city=city)
    else:
        flash('Failed to fetch weather data', 'error')
        return render_template('weather.html')
if __name__ == "__main__":
    app.run(port=5000)