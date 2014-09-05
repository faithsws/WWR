import web
from lxml import etree
import os
class WebIF:
		def __init__(self):
			self.urls = self.LoadWebPlugin()
		def LoadWebPlugin(self):
			urls = {}
			with open("WebPlugin" + os.sep + "config.xml") as f:
				dom = etree.fromstring(f.read())
				for plugin in dom:
					if plugin.tag == "plugin":
						modname = plugin.get("module")
						
						for url in plugin:
							clsname = url.get("class")
							#cls = getattr(mod,clsname)
							
							urls[url.get("path")] = modname+ "." +clsname
							
			return urls
		def AppendToApp(self,app):
			for (k,v) in self.urls.items():
				app.add_mapping(k,v)


