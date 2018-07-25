import webbrowser
import requests
import sys
#from bs4 import BeautifulSoup
def eng(filePath):
	#filePath = sys.argv[1]
	"""arg_len = len(sys.argv)
	#print(str(arg_len))
	if(arg_len!=2):
		print("Enter 1 image at a time")
		exit()"""
	searchUrl = 'http://www.google.hr/searchbyimage/upload'
	multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
	response = requests.post(searchUrl, files=multipart, allow_redirects=False)
	fetchUrl = response.headers['Location']
	
	webbrowser.open(fetchUrl)
"""if(r.status_code == 200):
	cont = r.content
	parser = {'html.parser', 'lxml'}
	for x in parser:
		soup = BeautifulSoup(cont, x)
		tag = soup.find_all("a")#,{"class":"fKDtNb"})
		print(str(len(tag))+" for "+str(x))
		for link in tag:
			print(str(link))"""

#eng("/home/scaars13/Pictures/Wallpapers/exp_sky.jpg")

