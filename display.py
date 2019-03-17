import webapp2
import jinja2
from mygpu import MyGpu
from google.appengine.ext import ndb
from datetime import datetime
from edit import Edit
import os

JINJA_ENVIRONMENT = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True
)

class Display(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        key = self.request.get('value')
        mygpu_key = ndb.Key('MyGpu', key)
        mygpuname = mygpu_key.get()
        template_values = {
         'mygpuname' : mygpuname
        }
        template =JINJA_ENVIRONMENT.get_template('display.html')
        self.response.write(template.render(template_values))


    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        if self.request.get('button') == 'Back':
            self.redirect('/')


        
