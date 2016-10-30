import urllib2 
import json
import requests
#  Website https://openweathermap.org/current
#  API Call:
#  http://api.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&cluster=yes&APPID={api key}
#  Data range for entire earth:
#  bbox=,-146,-60,160,55

# builds the api call for data from OpenWeatherMap.org
def build_api_call():
 	url = 'http://api.openweathermap.org/data/2.5/box/city?bbox=-160,-70,170,70&cluster=yes' 
 	url+='&{api key}'
	return url 
#loads the data from OpenWeatherMap in JSON format
def call_api(url):
	response = urllib2.urlopen(url)
	j = json.load(response)
	return j
# displays the JSON information so the data can easily be viewed, allows for easy changes to what data is collected
# prints the City name, lat, lon, temperature of the city, the rain data and the snow data of the city
def display_json(json_obj):
	print "DATA INCOMING!"
	x = 0
	for data in json_obj['list']:
		x += 1
		print "\nData Number: ",  x 
		print "City:", data['name']
		for key, value in data.iteritems():		
			if key == 'coord':
				print "Lon:", value['lon']
				print "Lat:", value['lat']
			elif key == 'main':
				print "Temperature in Celsius:", value['temp']
			elif key == 'rain':
				print "Rain Volume:", value['3h']
			elif key == 'snow':
				print "Snow Fall:", value['3h']
# creates a list in python that follows the same format needed for the WebGL Globe to accept 
# stats prints a list in the form [lat,lon,temp,lat,lon,temp....]
# this list is then copied into a JSON file for the globe to read
def parse_json(json_obj):
	stats = []
	for data in json_obj['list']:
		for key, value in data.iteritems():	
			if key == 'coord':
				lon = value['lon']
				lat = value['lat']
				stats = stats + [lat] + [lon]
			elif key == 'main':
				temp = value['temp']
				temp = temp / 30     # makes the temp values less than 1, so globe can view properly
				if temp < 0:
					temp = .0156
				stats = stats + [temp]
				
	print stats
		
url = build_api_call()
print "URL:",url
json_obj = call_api(url)
display_json(json_obj)
print "##############################"
parse_json(json_obj) # call to get globe data
