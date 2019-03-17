import webapp2
import jinja2
from mygpu import MyGpu
from google.appengine.ext import ndb
from datetime import datetime
import os

JINJA_ENVIRONMENT = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True
)

class Edit(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        mygpu = MyGpu()
        gpu = mygpu.name
        mygpu_key = ndb.Key('MyGpu', 'default')

        template_values = {
         'mygpu' : mygpu,

        }
        template =JINJA_ENVIRONMENT.get_template('edit.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        mygpu = MyGpu()

        if self.request.get('button') == 'Update':
            mygpu_key = ndb.Key('MyGpu', self.request.get('gpu_name'))
            my_gpu = mygpu_key.get()
            if my_gpu == None:
                mygpu = MyGpu(id=self.request.get('gpu_name'))
                mygpu.name = self.request.get('gpu_name')
                mygpu.manufacturer = self.request.get('manufacturer_name')
                mygpu.date = datetime.strptime(self.request.get('gpu_date'),'%Y-%m-%d')
                mygpu.geometryShader = bool(self.request.get('gpu_geometryShader'))
                mygpu.tesselationShader = bool(self.request.get('gpu_tesselationShader'))
                mygpu.shaderInt16 = bool(self.request.get('gpu_shaderInt16'))
                mygpu.sparseBinding = bool(self.request.get('gpu_sparseBinding'))
                mygpu.textureCompressionETC2 = bool(self.request.get('gpu_textureCompressionETC2'))
                mygpu.vertexPipelineStoresAndAtomics = bool(self.request.get('gpu_vertexPipelineStoresAndAtomics'))
                mygpu.put()

                self.redirect('/')
            else:
                self.redirect('/edit')

        elif self.request.get('button') == 'Cancel':
            self.redirect('/')
