import urllib2 
import json
import requests
#  Website https://openweathermap.org/current
#  API KEY:
#  b128a419a6c86255ac83d910112a3d5a  
#  API Call:
#  http://api.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&cluster=yes&APPID=b128a419a6c86255ac83d910112a3d5a
#  Data range for entire earth:
#  bbox=,-146,-60,160,55

def build_api_call():
 	url = 'http://api.openweathermap.org/data/2.5/box/city?bbox=-160,-70,170,70&cluster=yes' 
 	url+='&APPID=b128a419a6c86255ac83d910112a3d5a'
	return url 

def call_api(url):
	response = urllib2.urlopen(url)
	j = json.load(response)
	return j
			
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
				temp = temp / 30
				if temp < 0:
					temp = .0156
				stats = stats + [temp]
				
	print stats
		
url = build_api_call()
print "URL:",url
json_obj = call_api(url)
display_json(json_obj)
print "##############################"
parse_json(json_obj)
