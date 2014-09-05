# -*- coding: utf-8 -*-  
import os
import sys
import Utils
import web
import WebIF
import RouteIF
web.config.debug = False;
urls = (
	"/WeixinInterface","WeixinIF.WeixinIF"
	)
#import uuid
#def get_mac_address(): 
#	mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
#	return ":".join([mac[e:e+2] for e in range(0,11,2)])


app = web.application(urls,globals())
if __name__ == "__main__":
	webIf = WebIF.WebIF()
	webIf.AppendToApp(app)
	
	print(app.request("/login"))
#	ri = RouteIF.RouteIF()
#	ri.StartServer()
	#app.run()
#	event = '''<xml>
#<ToUserName><![CDATA[toUser]]></ToUserName>
#<FromUserName><![CDATA[FromUser]]></FromUserName>
#<CreateTime>123456789</CreateTime>
#<MsgType><![CDATA[event]]></MsgType>
#<Event><![CDATA[unsubscribe]]></Event>
#<EventKey><![CDATA[123333]]></EventKey>
#</xml>'''
#	print(app.request("/WeixinInterface","POST",event))\




#	text = '''<xml>
#<ToUserName><![CDATA[toUser]]></ToUserName>
#<FromUserName><![CDATA[FromUser]]></FromUserName>
#<CreateTime>123456789</CreateTime>
#<MsgType><![CDATA[text]]></MsgType>
#<Content><![CDATA[hello]]></Content>
#</xml>'''
#	print(app.request("/WeixinInterface","POST",text))
#	text = '''<xml>
#<ToUserName><![CDATA[toUser]]></ToUserName>
#<FromUserName><![CDATA[FromUser]]></FromUserName>
#<CreateTime>123456789</CreateTime>
#<MsgType><![CDATA[text]]></MsgType>
#<Content><![CDATA[hello1]]></Content>
#</xml>'''
#	print(app.request("/WeixinInterface","POST",text))
#	text = '''<xml>
#<ToUserName><![CDATA[toUser]]></ToUserName>
#<FromUserName><![CDATA[FromUser]]></FromUserName>
#<CreateTime>123456789</CreateTime>
#<MsgType><![CDATA[text]]></MsgType>
#<Content><![CDATA[hello]]></Content>
#</xml>'''
#	print(app.request("/WeixinInterface","POST",text))	
#	text = '''<xml>
#<ToUserName><![CDATA[toUser]]></ToUserName>
#<FromUserName><![CDATA[FromUser]]></FromUserName>
#<CreateTime>123456789</CreateTime>
#<MsgType><![CDATA[text]]></MsgType>
#<Content><![CDATA[hello1]]></Content>
#</xml>'''
#	print(app.request("/WeixinInterface","POST",text))
#	text = '''<xml>
#<ToUserName><![CDATA[toUser]]></ToUserName>
#<FromUserName><![CDATA[FromUser]]></FromUserName>
#<CreateTime>123456789</CreateTime>
#<MsgType><![CDATA[text]]></MsgType>
#<Content><![CDATA[gotoStat2e2]]></Content>
#</xml>'''
#	print(app.request("/WeixinInterface","POST",text))
#	text = '''<xml>
#<ToUserName><![CDATA[toUser]]></ToUserName>
#<FromUserName><![CDATA[FromUser]]></FromUserName>
#<CreateTime>123456789</CreateTime>
#<MsgType><![CDATA[text]]></MsgType>
#<Content><![CDATA[gotoStat2e2]]></Content>
#</xml>'''
#	print(app.request("/WeixinInterface","POST",text))
#	text = '''<xml>
#<ToUserName><![CDATA[toUser]]></ToUserName>
#<FromUserName><![CDATA[FromUser1]]></FromUserName>
#<CreateTime>123456789</CreateTime>
#<MsgType><![CDATA[text]]></MsgType>
#<Content><![CDATA[test]]></Content>
#</xml>'''
#	print(app.request("/WeixinInterface","POST",text))
#	
#	text = '''<xml>
#<ToUserName><![CDATA[toUser]]></ToUserName>
#<FromUserName><![CDATA[FromUser1]]></FromUserName>
#<CreateTime>123456789</CreateTime>
#<MsgType><![CDATA[event]]></MsgType>
#<Event><![CDATA[click]]></Event>
#<EventKey><![CDATA[]]></EventKey>
#</xml>'''
#	print(app.request("/WeixinInterface","POST",text))
#	while True:
#		import time
#		time.sleep(15.0)
#
#		text = '''<xml>
#<ToUserName><![CDATA[toUser]]></ToUserName>
#<FromUserName><![CDATA[FromUser]]></FromUserName>
#<CreateTime>123456789</CreateTime>
#<MsgType><![CDATA[text]]></MsgType>
#<Content><![CDATA[test]]></Content>
#</xml>'''
#		print(app.request("/WeixinInterface","POST",text))
#		text = '''<xml>
#	<ToUserName><![CDATA[toUser]]></ToUserName>
#	<FromUserName><![CDATA[FromUser]]></FromUserName>
#	<CreateTime>123456789</CreateTime>
#	<MsgType><![CDATA[text]]></MsgType>
#	<Content><![CDATA[gotoState1]]></Content>
#	</xml>'''
#		print(app.request("/WeixinInterface","POST",text))
#		text = '''<xml>
#	<ToUserName><![CDATA[toUser]]></ToUserName>
#	<FromUserName><![CDATA[FromUser]]></FromUserName>
#	<CreateTime>123456789</CreateTime>
#	<MsgType><![CDATA[text]]></MsgType>
#	<Content><![CDATA[gotoState1]]></Content>
#	</xml>'''
#		print(app.request("/WeixinInterface","POST",text))	
#		text = '''<xml>
#	<ToUserName><![CDATA[toUser]]></ToUserName>
#	<FromUserName><![CDATA[FromUser]]></FromUserName>
#	<CreateTime>123456789</CreateTime>
#	<MsgType><![CDATA[text]]></MsgType>
#	<Content><![CDATA[gotoState2]]></Content>
#	</xml>'''
#		print(app.request("/WeixinInterface","POST",text))
#		text = '''<xml>
#	<ToUserName><![CDATA[toUser]]></ToUserName>
#	<FromUserName><![CDATA[FromUser]]></FromUserName>
#	<CreateTime>123456789</CreateTime>
#	<MsgType><![CDATA[text]]></MsgType>
#	<Content><![CDATA[gotoStat2e2]]></Content>
#	</xml>'''
#		print(app.request("/WeixinInterface","POST",text))
#		text = '''<xml>
#	<ToUserName><![CDATA[toUser]]></ToUserName>
#	<FromUserName><![CDATA[FromUser]]></FromUserName>
#	<CreateTime>123456789</CreateTime>
#	<MsgType><![CDATA[text]]></MsgType>
#	<Content><![CDATA[gotoStat2e2]]></Content>
#	</xml>'''
#		print(app.request("/WeixinInterface","POST",text))
#		text = '''<xml>
#	<ToUserName><![CDATA[toUser]]></ToUserName>
#	<FromUserName><![CDATA[FromUser1]]></FromUserName>
#	<CreateTime>123456789</CreateTime>
#	<MsgType><![CDATA[text]]></MsgType>
#	<Content><![CDATA[test]]></Content>
#	</xml>'''
#		print(app.request("/WeixinInterface","POST",text))
#		
#		text = '''<xml>
#	<ToUserName><![CDATA[toUser]]></ToUserName>
#	<FromUserName><![CDATA[FromUser1]]></FromUserName>
#	<CreateTime>123456789</CreateTime>
#	<MsgType><![CDATA[text]]></MsgType>
#	<Content><![CDATA[gotoState2]]></Content>
#	</xml>'''
#		print(app.request("/WeixinInterface","POST",text))
