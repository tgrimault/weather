#!/usr/bin/env python
import json
from urllib2 import urlopen

class WForecast:
	date = []
	time = []
	temp = []
	weather = []
	nbOfForecast = 0

	def __init__(self):
		data = urlopen('http://api.openweathermap.org/data/2.1/forecast/city?q=Beloeil,qc&units=metric')
		forecasts = json.load(data)
		for forecast in forecasts['list']:
			full_date = forecast['dt_txt'].split(' ')
			self.date.append(full_date[0])
			self.time.append(full_date[1])
			self.temp.append(forecast['main']['temp'])
			self.weather.append(forecast['weather'][0]['main'])
			self.nbOfForecast += 1

	def __getitem__(self):
		return self



forecast = WForecast()
separator = "*************************************"

for i in range(0, forecast.nbOfForecast):
	print forecast.date[i]
	print forecast.time[i]
	print forecast.temp[i]
	print forecast.weather[i]
	print separator

