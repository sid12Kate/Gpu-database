import webapp2
import jinja2
from mygpu import MyGpu
from google.appengine.ext import ndb
from datetime import datetime
from edit import Edit
from display import Display
import os

JINJA_ENVIRONMENT = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True
)

class EditGpu(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        key = self.request.get('value')
        mygpu_key = ndb.Key('MyGpu', key)
        mygpuname = mygpu_key.get()
        template_values = {
         'mygpuname' : mygpuname
        }
        template =JINJA_ENVIRONMENT.get_template('editgpu.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        mygpu = MyGpu()
        if self.request.get('button') == 'Update':

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
        elif self.request.get('button') == 'Cancel':
            self.redirect('/')
