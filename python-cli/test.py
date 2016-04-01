#import ssl

from firebase import firebase
#ssl._create_unverified_https_context = ssl._create_unverified_context
firebase = firebase.FirebaseApplication('https://manit.firebaseio.com/',None)


#if (raw_input("\n 1. News \t 2. Events \n Enter among the above options:") == '1'):


newItemId = raw_input("Enter the unique id: ")
newSubmittedBy= raw_input("Enter your name: ")
newType = raw_input("Enter the type: ")
newTitle = raw_input("Enter the title for the news: ")
newPickUpLine = raw_input("Enter the pick up line for the news: ")
newContent = raw_input("Enter the content for the news: ")
newUrl = raw_input("Enter the url of the news: ")

data={'id':newItemId, 'title':newTitle, 'content':newContent, 'pickupline':newPickUpLine, 'by':newSubmittedBy, 'type':newType, 'url':newUrl}

result = firebase.put('/news', newItemId, data)

print (result)

newsLayout = firebase.get('/news',None)

print (newsLayout)


