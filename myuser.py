from google.appengine.ext import ndb

class MyUser(ndb.Model):
    uname = ndb.StringProperty()
