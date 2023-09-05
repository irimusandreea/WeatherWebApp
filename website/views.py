from flask import Blueprint, render_template
import requests

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("Home.html")

@views.route('/newyork')
def get_nyweather():
    api_key = '742c6514cbef4e8a9aec2fec73ef6aeb'
    url = f'http://api.openweathermap.org/data/2.5/weather?q=New York City&appid={api_key}&units=metric'
    ny_weather = {}

    response_ny = requests.get(url)

    if response_ny.status_code == 200:
        ny_weather = response_ny.json()

    return render_template("NYC.html", ny_weather=ny_weather)

@views.route('/houston')
def get_huweather():
    api_key = '742c6514cbef4e8a9aec2fec73ef6aeb'
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Houston&appid={api_key}&units=metric'
    hu_weather = {}

    response_hu = requests.get(url)

    if response_hu.status_code == 200:
        hu_weather = response_hu.json()

    return render_template("Houston.html", hu_weather=hu_weather)