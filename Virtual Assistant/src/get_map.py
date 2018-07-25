import webbrowser
import text_speech
def find_on_map(topic):
	try:
		text_speech.say("Opening "+topic+" on google maps")
		webbrowser.open("https://www.google.nl/maps/place/" + topic + "/&amp;")
	except:
		text_speech.say("Some error occured.")

#find_on_map("Siwa")