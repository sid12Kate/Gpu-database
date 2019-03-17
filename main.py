import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from myuser import MyUser
from edit import Edit
from mygpu import MyGpu
from editgpu import EditGpu
from display import Display
from search import Search
from compare import Compare
from compareresult import CompareResult
import os

JINJA_ENVIRONMENT = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        mygpu = MyGpu()
        url = ''
        url_string = ''
        welcome = 'Welcome back'
        myuser = None

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_string = 'logout'

            myuser_key = ndb.Key('MyUser', user.email())
            myuser = myuser_key.get()

            if myuser == None:
                welcome = 'Welcome to the application'
                myuser = MyUser(id=user.email())
                myuser.put()
        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'login'


        gpu_list = mygpu.query().fetch()
        template_values = {
        'url' : url,
        'url_string' : url_string,
        'user' : user,
        'welcome' : welcome,
        'myuser' : myuser,
        'mygpu'  : mygpu,
        'gpu_list' : gpu_list
        }

        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/edit', Edit),
    ('/display',Display),
    ('/editgpu',EditGpu),
    ('/search',Search),
    ('/compare',Compare),
    ('/compareresult',CompareResult),
], debug=True)
