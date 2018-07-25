from weather import Weather, Unit
import location
import text_speech

def weather_loc(location):
	text_speech.say("weather and forecast of "+location)
	weather = Weather(unit=Unit.CELSIUS)
	location = weather.lookup_by_location(location)
	condition = location.condition
	#print(condition.text)
	print("Last updated "+condition.date+" Condition :- "+condition.text)
	forecasts = location.forecast
	#print(len(forecasts))
	for forecast in forecasts:
	    print("On date "+forecast.date+" Condition :- "+forecast.text+" High :- "+forecast.high+" Low :- "+forecast.low)

def get_local_weather():
	loc = location.get_city()
	if(loc=="-1"):
		return -1
	else:
		weather_loc(loc)
#get_local_weather()