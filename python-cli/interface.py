#import ssl

from firebase import firebase
#ssl._create_unverified_https_context = ssl._create_unverified_context
firebase = firebase.FirebaseApplication('https://manit.firebaseio.com/',None)
flag = 0

# Get the top level id
f=open('tmp.txt','r+') 
valn = f.readline()
vale = f.readline()
idn, ide = int(valn), int(vale)
f.seek(0,0)

if (raw_input("\n 1. News \t 2. Events \n Enter among the above options:") == '2'):
	flag = 1
	newEventDate = raw_input("DATE: ")
	newEventTime = raw_input("TIME: ")
	newEventVenue = raw_input("LOCATION: ")
	ide +=  1
	idn -=  1
	eventInx = str(ide)

idn += + 1
newSubmittedBy= raw_input("AUTHOR: ")
newType = raw_input("TYPE: ")
newTitle = raw_input("TITLE: ")
newPickUpLine = raw_input("STORY LINE: ")
newContent = raw_input("CONTENT: ")
newUrl = raw_input("URL: ")


if flag == 1 :
	data={'id':eventInx, 'title':newTitle, 'content':newContent, 'pickupline':newPickUpLine, 'by':newSubmittedBy, 'type':newType, 'url':newUrl, 'date':newEventDate, 'time':newEventTime, 'location':newEventVenue}
	result = firebase.put('/event', eventInx, data)
else:
	newsIndex = str(idn)
	data={'id':newsIndex, 'title':newTitle, 'content':newContent, 'pickupline':newPickUpLine, 'by':newSubmittedBy, 'type':newType, 'url':newUrl}
	result = firebase.put('/news', newsIndex, data)

f.write(str(idn) + '\n' + str(ide))
f.close()

print (result)



