import datetime as dt 
import requests


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "14ee6ff1334128f8ec6367802c595f6b"
CITY = "Nairobi"

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    farenheit = celsius * (9/5) + 32
    return celsius, farenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahreinheit = kelvin_to_fahrenheit(temp_kelvin)

print (response)
print("Temperature in Celsius:", temp_celsius)