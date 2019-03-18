import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from mygpu import MyGpu
import os

JINJA_ENVIRONMENT = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True
)

class Compare(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        mygpu = MyGpu()

        gpu_list = MyGpu().query().fetch()
        template_values = {
        # 'mygpu' : mygpu,
        'gpu_list' : gpu_list
        }

        template = JINJA_ENVIRONMENT.get_template('compare.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        if self.request.get('button') == 'Compare':
            v1 = self.request.get('v_1')
            v2 = self.request.get('v_2')
            if v1 == v2:
                self.response.write('Please select two different gpus')
            else:
                self.redirect('/compareresult?value_1='+v1+ '&value_2='+v2)
