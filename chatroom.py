from google.appengine.api import users
from google.appengine.ext import ndb
import datetime
import webapp2
import urllib

DEFAULT_CHAT_ROOM_NAME = "chatroom"


class ChatUser(ndb.Model):

    user_name = ndb.StringProperty(indexed=False)
    user_email = ndb.StringProperty(indexed=False)
    user_id = ndb.StringProperty(indexed=False)


class Chat(ndb.Model):

    chat_user = ndb.StructuredProperty(ChatUser)
    message = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


def chatroom_key(chat_room = DEFAULT_CHAT_ROOM_NAME):
    return ndb.Key('Chatroom', chat_room)


class MainPage(webapp2.RequestHandler):

    def post(self):
        user_email = users.get_current_user().email()
        user_id = users.get_current_user().user_id()
        user_name = users.get_current_user().nickname()

        chat_room = self.request.get('chatroom_name', DEFAULT_CHAT_ROOM_NAME)

        chat = Chat(parent=chatroom_key(chat_room))
        chat.message = self.request.get('content')
        if users.get_current_user():
            chat.chat_user = ChatUser(user_name=user_name, user_email=user_email, user_id=user_id)
        chat.put()

        query_params = {'chatroom_name': chat_room}
        self.redirect('/?' + urllib.urlencode(query_params))

    def get(self):

        chat_user = users.get_current_user()
        print chat_user
        print "user printed"

        if chat_user is None:
            print "entered None"
            self.redirect(users.create_login_url(self.request.uri))
        else:
            self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
            self.response.write('Hello, ' + chat_user.nickname()+' - <a href="/logout">logout</a>')
            self.response.out.write(
                """
                <html>
                <head>
                <meta http-equiv="refresh" content="15"/>
                <title>Welcome to Chat Room Messenger</title></head>
                <body>
                    <h3>Chat Room Messenger </h3>"""
            )

            chat_room = self.request.get('chatroom_name', DEFAULT_CHAT_ROOM_NAME)
            chats_query = Chat.query(
                ancestor=chatroom_key(chat_room)).order(Chat.date)
            chats = chats_query.fetch(40)

            self.response.out.write("""
            <div>
            <textarea rows="25" cols="90" readonly>""")
            for each_chat in chats:
                self.response.out.write("%s:%s\n" %(each_chat.chat_user.user_name,each_chat.message))

            self.response.out.write("""
            </textarea>
            </div>
            """)
            self.response.out.write("""<br>""")
            self.response.out.write("""
            <form action="" method="post">
            <div>
            <textarea name="content" rows="4" cols="90"></textarea>
            <input type="submit" value="Send" height="20"></input>
            </div>
            <div>

            <div>
            </form>
            </body>
            </html>"""
                                    )

class Chat_logout(webapp2.RequestHandler):

    def get(self):
        self.redirect(users.create_logout_url('/'))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/logout', Chat_logout),
], debug=True)