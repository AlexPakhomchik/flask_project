from flask import Flask, request, render_template
import requests

from KEYS import afgani
from relation_load import relation
import csv

app = Flask(__name__)

relation()


@app.route('/')
def home():
    return render_template('home_page.html')


@app.route('/1')
def weather():
    name = 'Погода'
    response = requests.get(
        'https://api.open-meteo.com/v1/forecast?latitude=33.34&longitude=44.40&current_weather=true&past_days=1').json()
    qwe = str(response['current_weather']['temperature'])
    return render_template('Weather_page.html', name=name, weather=qwe)


@app.route('/2')
def currency():
    response = requests.get(
        afgani).json()
    asd = str(response['data']['USD']['value'])
    return render_template('Currency_page.html', currency=asd)


@app.route('/3')
def relation_weather_and_currency():
    list_relation = []
    with open("weather_and_currency.csv", 'r', encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        count = 0
        for row in file_reader:
            list_relation.append(row)
            count += 1
    return render_template('Relation_weather_and_currency.html', relation=list_relation)


if __name__ == '__main__':
    app.run(debug=True)
