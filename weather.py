#!/usr/bin/env python
import json
from urllib2 import urlopen
from pprint import pprint

data = urlopen('http://api.openweathermap.org/data/2.1/forecast/city?q=Beloeil,qc&units=metric')
forcasts = json.load(data)
for forcast in forcasts['list']:
	pprint(forcast['dt_txt'])
	pprint(forcast['main'])
	pprint(forcast['weather'])

