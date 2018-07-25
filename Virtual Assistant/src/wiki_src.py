import wikipedia
import web_browser
import os
import text_speech
import sys

def open_wiki(topic):
	
	try:
		page = wikipedia.page(topic)
	except:
		text_speech.say("Sorry, Some error occured. Are you sure this topic is on wikipedia")
		return 1
	text_speech.say('Getting the url')
	link = page.url
	web_browser.open_link(link)
	return 0

#open_wiki('Messi')