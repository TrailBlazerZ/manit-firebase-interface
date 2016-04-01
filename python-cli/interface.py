#import ssl

from firebase import firebase
#ssl._create_unverified_https_context = ssl._create_unverified_context
firebase = firebase.FirebaseApplication('https://manit.firebaseio.com/news/',None)
flag = 0

if (raw_input("\n 1. News \t 2. Events \n Enter among the above options:") == '2'):
	flag = 1
	newEventDate = raw_input("DATE: ")
	newEventTime = raw_input("TIME: ")
	newEventVenue = raw_input("LOCATION: ")

newItemId = raw_input("UNIQUE ID: ")
newSubmittedBy= raw_input("AUTHOR: ")
newType = raw_input("TYPE: ")
newTitle = raw_input("TITLE: ")
newPickUpLine = raw_input("STORY LINE: ")
newContent = raw_input("CONTENT: ")
newUrl = raw_input("URL: ")


if flag == 1 :
	data={'id':newItemId, 'title':newTitle, 'content':newContent, 'pickupline':newPickUpLine, 'by':newSubmittedBy, 'type':newType, 'url':newUrl, 'date':newEventDate, 'time':newEventTime, 'location':newEventVenue}
	result = firebase.put('/event', newItemId, data)
else:
	data={'id':newItemId, 'title':newTitle, 'content':newContent, 'pickupline':newPickUpLine, 'by':newSubmittedBy, 'type':newType, 'url':newUrl}
	result = firebase.put('/news', newItemId, data)

print (result)



