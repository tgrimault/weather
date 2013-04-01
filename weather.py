#!/usr/bin/env python
import json
from urllib2 import urlopen
from pprint import pprint

data = urlopen('http://api.openweathermap.org/data/2.1/forecast/city?q=Beloeil,qc&units=metric')
forecasts = json.load(data)
for forecast in forecasts['list']:
	full_date = forecast['dt_txt'].split(' ')
	date = full_date[0]
	time = full_date[1]
	temp = forecast['main']['temp']
	weather = forecast['weather'][0]['main']
	print date
	print time
	print temp
	print weather
	separator = "*************************************"
	print separator

