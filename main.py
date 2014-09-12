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

text = '''
<xml>
  <ToUserName><![CDATA[2ed53c061ebf170ac3061cd18d77b7a0]]></ToUserName>
  <FromUserName><![CDATA[f9bc3e4fd68b4dbdc3061cd18d77b7a0]]></FromUserName>
  <CreateTime>1409904215</CreateTime>
  <MsgId>74</MsgId>
  <MsgType><![CDATA[text]]></MsgType>
  <Content><![CDATA[down]]></Content>
</xml>

'''

app = web.application(urls,globals())
if __name__ == "__main__":
	webIf = WebIF.WebIF()
	webIf.AppendToApp(app)

	if'win32' == sys.platform:
		print(app.request("/WeixinInterface",method="POST",data=text))
	else:
		print(app.mapping)
		app.run()	
