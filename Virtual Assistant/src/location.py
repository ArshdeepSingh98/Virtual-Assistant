import requests
import json
from geopy.geocoders import Nominatim
def get_area():
	send_url = 'http://freegeoip.net/json'
	r = requests.get(send_url)
	j=json.loads(r.text)
	lat = j['latitude']
	lon = j['longitude']
	#print(str(lat)+"  "+str(lon))

	geolocator = Nominatim()
	pair_coord = str(lat)+", "+str(lon)
	location = str(geolocator.reverse(pair_coord, exactly_one = True))
	return location

def get_city():
	count=0
	while(count<4):
		try:
			city = get_area().split(',')[-4]
			return city
		except:
			count+=1
	print("geocode timed out on various attempts. Check your connectivity or try again.")
	return "-1"
#print(get_area())