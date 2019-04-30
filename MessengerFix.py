from bs4 import BeautifulSoup
import codecs, tkFileDialog, re, time, datetime

def FBMessageCleaner():
	filepath = tkFileDialog.askopenfilename()
	SaveFile( CleanFile( OpenFile(filepath) ), GetSaveLocation(filepath) )

def OpenFile(file):
	entirehtml = codecs.open(file, 'r')	
	return entirehtml

def CleanFile(document):
	regex = re.compile('\\d{2}/\\d{2}/\\d{4},.\\d{2}:\\d{2}')
	CleanStartTime = time.time()
	cleaned = BeautifulSoup(document, "lxml").get_text()
	cleaned = cleaned.split(" ")
	if(len(cleaned) < 290):
		print("Wrong type of file, please choose a facebook messenger history file.")
		quit()
	else:
		for i in range(290):
			cleaned.pop(0)
	cleaned =  " ".join(cleaned)
	cleanedwregex = re.split(regex, cleaned)
	listofdates = re.findall(regex, cleaned)
	CleanEndTime = time.time()
	print("HTML cleaned in " + str("%.2f" % (CleanEndTime - CleanStartTime)) + "seconds")

	PrintStartTime = time.time()
	gucciString = ""
	for i in range(len(cleanedwregex) - 1):
		gucciString += listofdates[i] + " | " + cleanedwregex[i] + "\n"

	print(gucciString)
	PrintEndTime = time.time()
	print("Printed to console in " + str("%.2f" % (PrintEndTime - PrintStartTime)) + "seconds")
	
	return gucciString

def SaveFile(text, location):
	text = unicode(text).encode('utf-8')
	with open(location, "w") as text_file:
		text_file.write(text)
	print("Clean file saved in:" + location)

def GetSaveLocation(file):
	path = file.split('/')
	if( '_' in path[len(path) - 2]) :
		#If user is using the default extracted folder (/messages/inbox/NAME_ID/Message.html)
		filename = path[len(path) - 2].split('_')[0] + "_CLEAN-" + str(datetime.datetime.now()).split('.')[0]
	else:	
		#If user is using the file from somewhere else
		filename = "CLEAN_CHAT-" + str(datetime.datetime.now()).split('.')[0]
	del path[-1]
	path.insert(len(path), filename + ".txt")
	path = "/".join(path)
	return path
	
FBMessageCleaner()
