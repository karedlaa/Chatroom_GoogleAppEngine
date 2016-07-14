Chatroom 

These web services are for user log in and storing their messages on the chat window to create a basic chat room system.
HTML body is used to design page.

WebService1: Google User Management

user login:
$ curl https://accounts.google.com/ServiceLogin?service=ah&passive=true&continue=https%3A%2F%2Fappengine.google.com%2F_ah%2Fconflogin%3Fcontinue%3Dhttp%3A%2F%2Fchat-room-1233.appspot.com%2F&ltmpl=gm&shdf=ChULEgZhaG5hbWUaCWNoYXQtcm9vbQwSAmFoIhQPBG9DleBI37r0gykQs92GAcfbqCgBMhSMoFcbOPHgdORFd7RPOyyxIaIVgg

logout after using the chat system

Example usage:

login with mail ID: anuk1384@gmail.com

It is redirected to
$ curl http://chat-room-1233.appspot.com/

hello, anuk1384

WebService2: App Engine Datastore

data storage window:

$ curl http://chat-room-1233.appspot.com/?chatroom_name=chatroom

Example usage: after log in

anuk1384:  Hi

madh.anchuri:  Hi

On the localhost:

To check the Datastore viewer(Date, time, user details):
$ curl http://localhost:8000/datastore?kind=Chat

To view the datastore indexes(index.yaml):
$ curl http://localhost:8000/datastore-indexes

Deploy the application into google cloud using the command:
[Example: Project Folder = chatengine/]

$ appcfg.py -A chat-room-1233 update chatengine/

Using the Project ID: chat-room-1233

Visit this application using URL: http://chat-room-1233.appspot.com/


refreshing the page for every 15sec 
constraint: message should be typed and send in 15 sec.

Future Work: Using AJAX, synchronizing the chat window and dealing with the given constraint to be gone

