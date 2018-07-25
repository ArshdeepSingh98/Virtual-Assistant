import sys
sys.path.insert(0,'src')
import get_news
import text_speech
import wiki_src
import file_search
import img_srch
import speech_text
import dev_handle
import get_weather
import you_down
import time
import get_map


sys.path.insert(0,'chat_dir')
import dumb_chatbot
text_speech.say("Hello, How may I help You?")
text_input = raw_input()


while(text_input!="exit"):
	if(text_input == "lock device"):
		try:

			dev_handle.lock_device()
		except:
			text_speech.say("Sorry. An error was encountered.")
	elif(text_input=="restart device"):
		try:
			text_speech.say("Restarting device.")
			time.sleep(5)
			dev_handle.restart()
		except:
			text_speech.say("Sorry. An error was encountered")
	elif(text_input=="shut down device"):
		try:
			text_speech.say("Shutting down device.")
			time.sleep(5)
			dev_handle.shut_down()
		except:
			text_speech.say("Sorry. An error was encountered")
	elif(text_input=="get local weather"):
		try:
			text_speech.say("Getting local weather")
			get_weather.get_local_weather()
		except:
			text_speech.say("Sorry an error was encountered")
	elif(text_input=="search wikipedia"):
		try:
			text_speech.say("What do you want to search on Wikipedia?")
			text_input1 = raw_input()
			text_speech.say("Searching Wikipedia")
			wiki_src.open_wiki(text_input1)
		except:
			text_speech.say("Sorry. An error was encountered.")
	elif(text_input=="search file"):
		try:
			text_speech.say("Enter the name of the file you want to search")
			text_input1 = raw_input()
			file_search.find_all(text_input1,"/home")
		except:
			text_speech.say("Sorry. An error was encountered.")
	elif(text_input=="stream video"):
		try:
			text_speech.say("Enter the name of video you want to stream")
			text_input1 = raw_input()

			you_down.stream_video(text_input1)
		except:
			text_speech.say("Sorry, An error was encountered.")
	elif(text_input=="download video"):
		#try:
		text_speech.say("Enter the name of video you want to download")
		text_input1 = raw_input()
		you_down.download_video(text_input1)
		#except:
		#	text_speech.say("Sorry, An error was encountered.")
	elif(text_input == "find location"):
		try:
			text_speech.say("Enter the location you want to find.")
			text_input1 = raw_input()
			get_map.find_on_map(text_input1)
		except:
			text_speech.say("Sorry, An error was encountered.")
	elif((text_input == "reverse image search") or (text_input == "recognise image")):
		try:
			text_speech.say("Enter the location of image you want to search or recognise")
			text_input1 = raw_input()
			text_speech.say("Searching Image")
			img_srch.eng(text_input1)
		except:
			text_speech.say("Sorry. An error was encountered.")
	elif(text_input=="get local news"):
		try:
			text_speech.say("Getting local news")
			get_news.get_local_news()
		except:
			text_speech.say("Sorry. An error was encountered.")
	elif(text_input=="get topic news"):
		try:
			text_speech.say("Enter the topic on which you want to get news")
			text_input1 = raw_input()
			get_news.get_news(text_input1)
		except:
			text_speech.say("Sorry an error was encountered.")
	elif(text_input=="get location weather"):
		try:
			text_speech.say("Enter the location")
			text_input1 = raw_input()
			get_weather.weather_loc(text_input1)
		except:
			text_speech.say("Sorry an error was encountered.")
	elif(text_input == "chat"):
		try:
			text_speech.say("Opening Chatbot")
			dumb_chatbot.chat()
		except:
			text_speech.say("Sorry an error was encountered.")
	else:
		try:
			text_speech.say("Please enter a valid command.")
		except:
			text_speech.say("Sorry an error was encountered.")	
	text_speech.say("Anything else I can help you with?")
	text_input = raw_input()
	text_input = text_input.lower()
