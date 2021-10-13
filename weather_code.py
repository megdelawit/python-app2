import requests
import csv

def getWeather(city_names):
    weather = []

    for city in city_names:
        complete_url = base_url + "appid=" + api_key + "&q=" + city

        response = requests.get(complete_url)

        weather.append(response.json())

    return weather

def writeCSV(data):

    outputFile = open('/tmp/weather.csv', 'w', newline='') 

    outputWriter = csv.writer(outputFile)

    outputWriter.writerow(['Name', 'main', 'temp'])

    for weather in data:
        outputWriter.writerow([weather['name'], weather['weather'][0]['main'], weather['main']['temp']])


api_key = "a88abc506b9126f01f4807d817fbcf8d"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_names = ['Fortaleza', 'Sao Paulo', 'Dallas', 'Mexico City']

    
weather = getWeather(city_names)

print(weather)


writeCSV(weather)

