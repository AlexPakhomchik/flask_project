import csv
import requests
import datetime

from KEYS import afgani


def relation():
    response_weather = requests.get(
        'https://api.open-meteo.com/v1/forecast?latitude=33.34&longitude=44.40&current_weather=true&past_days=1').json()
    qwe = str(response_weather['current_weather']['temperature'])
    response_currency = requests.get(
        afgani).json()
    asd = str(response_currency['data']['USD']['value'])

    date_object = datetime.date.today()

    with open("weather_and_currency.csv", mode="a", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=",", lineterminator="\n")
        file_writer.writerow([date_object, qwe, asd])
