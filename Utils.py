from lxml import etree


def LoadConfigFile(filename="config.xml"):
		urls = []
		wxProcessors = {"event":[],"text":[]}
		routeIfSetting = {}
		with open(filename) as f:
				xmlString = f.read()
				dom = etree.fromstring(xmlString)
								
				routeIf = dom.find("RouteIF")
				serverSetting = routeIf.find("server")
				
				routeIfSetting["port"] 	= int(serverSetting.get("port"))	
				routeIfSetting["maxConnections"] = int(serverSetting.get("maxConnections"))	
				#print(wxProcessors)
				
		return {"WebUrls":urls,"WeixinProcessors":wxProcessors,"RouteIF":routeIfSetting}	

PluginConfig = LoadConfigFile()
