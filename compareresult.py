import webapp2
import jinja2
from mygpu import MyGpu
from google.appengine.ext import ndb
import os

JINJA_ENVIRONMENT = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True
)

class CompareResult(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        mygpu = MyGpu()
        key_1 = self.request.get('value_1')
        key_2 = self.request.get('value_2')

        mygpu_key_1 = ndb.Key('MyGpu', key_1)
        mygpu_key_2 = ndb.Key('MyGpu', key_2)

        mygpu_1 = mygpu_key_1.get()
        mygpu_2 = mygpu_key_2.get()

        #if mygpu_1 == mygpu_2 :
            #self.redirect('/')

        template_values = {
         'mygpu_1' : mygpu_1,
         'mygpu_2' : mygpu_2
        }
        template =JINJA_ENVIRONMENT.get_template('compareresult.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        mygpu = MyGpu()
        if self.request.get('button') == 'Back':
            self.redirect('/')
