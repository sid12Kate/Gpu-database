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

class Search(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        mygpu = MyGpu()
        gpu = mygpu.name
        mygpu_key = ndb.Key('MyGpu', 'default')

        mygpu.geometryShader = bool(self.request.get('gpu_geometryShader'))
        mygpu.tesselationShader = bool(self.request.get('gpu_tesselationShader'))
        mygpu.shaderInt16 = bool(self.request.get('gpu_shaderInt16'))
        mygpu.sparseBinding = bool(self.request.get('gpu_sparseBinding'))
        mygpu.textureCompressionETC2 = bool(self.request.get('gpu_textureCompressionETC2'))
        mygpu.vertexPipelineStoresAndAtomics = bool(self.request.get('gpu_vertexPipelineStoresAndAtomics'))


        gpu_list = mygpu.query()
        if self.request.get('button') == 'Search':

            if mygpu.geometryShader == True:
                gpu_list = gpu_list.filter(MyGpu.geometryShader == True)
            if mygpu.tesselationShader == True:
                gpu_list = gpu_list.filter(MyGpu.tesselationShader == True)
            if mygpu.shaderInt16 == True:
                gpu_list = gpu_list.filter(MyGpu.shaderInt16 == True)
            if mygpu.sparseBinding == True:
                gpu_list = gpu_list.filter(MyGpu.sparseBinding == True)
            if mygpu.textureCompressionETC2 == True:
                gpu_list = gpu_list.filter(MyGpu.textureCompressionETC2 == True)
            if mygpu.vertexPipelineStoresAndAtomics == True:
                gpu_list = gpu_list.filter(MyGpu.vertexPipelineStoresAndAtomics == True)
            gpus = gpu_list.fetch()

        else:
            gpus = ""


        template_values = {
         'mygpu' : mygpu,
         'gpus' : gpus
        }

        template =JINJA_ENVIRONMENT.get_template('search.html')
        self.response.write(template.render(template_values))


    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        mygpu = MyGpu()
        if self.request.get('button') == 'Back':
            self.redirect('/')
