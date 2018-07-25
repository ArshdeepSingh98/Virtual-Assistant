import webbrowser
import os
import text_speech
def find_all(name, path):
	text_speech.say("Searching Your Desktop")
	count=0
	result = []
	for root, dirs, files in os.walk(path):
   		if name in files:
			match = os.path.join(root, name)
			result.append(match)
			webbrowser.open(match)
			count+=1
			if(count>=1):
				break
	text_speech.say(str(len(result))+" results found.")


#find_all("exp_sky.jpg","/home")