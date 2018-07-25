import webbrowser
import sys
import text_speech

def open_link(link):
	try:
		webbrowser.open(link)
	except:
		text_speech.say("Sorry, Some error occured while opening the link.")