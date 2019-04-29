from bs4 import BeautifulSoup
import codecs
import tkFileDialog
import re
import time
import os

def FBMessageCleaner():
	CleanFile(OpenFile())

def OpenFile():
	file = tkFileDialog.askopenfilename()
	startTime = time.time()
	entirehtml = codecs.open(file, 'r')	
	endTime = time.time()
	print("File opened in " + str("%.2f" % (endTime - startTime)) + "seconds")
	return entirehtml

def CleanFile(document):
	regex = re.compile('\\d{2}/\\d{2}/\\d{4},.\\d{2}:\\d{2}')
	startTime = time.time()
	cleaned = BeautifulSoup(document, "lxml").get_text()
	cleaned = cleaned.split(" ")
	for i in range(290):
		cleaned.pop(0)
	cleaned =  " ".join(cleaned)
	cleanedwregex = re.split(regex, cleaned)
	listofdates = re.findall(regex, cleaned)
	endTime = time.time()
	if(len(listofdates) == 0):
		print("No dates found, please choose a facebook messenger history file.")
		quit()
	print("HTML cleaned in " + str("%.2f" % (endTime - startTime)) + "seconds")

	gucciString = ""
	for i in range(len(cleanedwregex) - 1):
		gucciString += listofdates[i] + " | " + cleanedwregex[i] + "\n"

	gucciString = unicode(gucciString).encode('utf-8')
	print(gucciString)

	if os.name == 'nt':
		desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
	else:
		desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

	with open(desktop + "/CleanedMessage.txt", "w") as text_file:
   	 text_file.write(gucciString)
   	 print("Clean file saved in:" + desktop + "/CleanedMessage.txt")


FBMessageCleaner()
