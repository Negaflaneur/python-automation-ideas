import os
import json, requests, sys
from pprint import pprint

app_id = os.environ.get('open_weather_map')

##download data from open weather map
url = f'https://api.openweathermap.org/data/2.5/weather?lat=52.2&lon=0.11&appid={app_id}'
response = requests.get(url)
response.raise_for_status()

#printing data
weatherData = json.loads(response.text)

pprint(response.text)
