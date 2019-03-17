from google.appengine.ext import ndb

class MyGpu(ndb.Model):
    name = ndb.StringProperty()
    manufacturer = ndb.StringProperty()
    date = ndb.DateProperty()
    geometryShader = ndb.BooleanProperty()
    shaderInt16 = ndb.BooleanProperty()
    sparseBinding = ndb.BooleanProperty()
    textureCompressionETC2 = ndb.BooleanProperty()
    vertexPipelineStoresAndAtomics = ndb.BooleanProperty()
    tesselationShader = ndb.BooleanProperty()
