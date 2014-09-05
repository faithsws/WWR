# -*- coding: utf-8 -*-  
import os
import sys
import Utils
import web
import WebIF
import RouterIF
import WeixinIF
web.config.debug = False;
urls = (
	"/WeixinInterface","WeixinIF.WeixinIF"
	)


app = web.application(urls,globals())
if __name__ == "__main__":
	webIf = WebIF.WebIF()
	webIf.AppendToApp(app)

	app.run()	
