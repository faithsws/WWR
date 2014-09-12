# -*- coding: utf-8 -*-  
import web
import hashlib
from lxml import etree
import Utils
import os
import sys
import time
import threading
import copy
import urllib2
import json
TOKEN="sws"
APPID="e09b8bc600924e119b7e2ada7c9e732e"
APPSECRET="9e5e255727fb4e33b958d648ac781ab3"
class TextPlugin:
	def __init__(self,xml,ctx):
		self.xml = xml
		self.ctx = ctx
		self.statePair = {}
		self.LoadStateClass()
		self.LoadStateMachine()
		self.curState = self.statePair["Original"]
		
	def LoadStateClass(self):
		classname = self.xml.get("class")
		for child in self.xml:
			if child.tag == "state":
				if '.' in classname:
					modname, clsname = classname.rsplit('.', 1)
					mod = __import__(modname)
				else:
					clsname = classname
					mod = sys.modules[__name__]

				cls = getattr(mod,child.get("class"),None)
				if cls == None:
					raise Exception("no class named " + child.get("class"))
				clsEntry = cls(self,{"enter":child.get("enterTips"),"process":child.get("processTips")})                    
				self.statePair[child.get("name")] = clsEntry;
	def LoadStateMachine(self):
		for child in self.xml:
			if child.tag == "state":
				state = self.statePair[child.get("name")]
				for item in child:
					if item.tag == "action":
						state.target[item.get("inputText")] = self.statePair[item.get("targetState")]		
					if item.tag == "process":
						state.processor[item.get("inputText")] = item.get("returnText")
			
	def Process(self,text):
		if text in self.curState.target:
			return self.ChangeState(self.curState.target[text],text)
		else:
			return self.curState.Process(self,text)
	def ChangeState(self,state,text):
		self.curState.Leave(self,text)
		self.curState = state
		return state.Enter(self,text)

class State:
	def __init__(self,plugin,tips):
		self.target = {}
		self.processor = {}
		self.plugin = plugin
		self.tips = tips
	def Enter(self,ctx,text):
		return self.tips["enterTip"]
	def Process(self,ctx,text):
		for (k,v) in self.processor.items():
			if k == text:
				return v
		else:
			return "unknown command"
	def Leave(self,ctx,text):
		raise NotImplementedError()


class EventPlugin:
	def __init__(self,ctx):
		self.processor = {"subscribe":self.OnSubscribe,"unsubscribe":self.OnUnsubscribe,"click":self.OnClick,"LOCATION":self.OnLocation,"ENTER":self.OnLocation}
		self.messages = {}
		self.ctx = ctx
	def Process(self,usr,event,key):
		for (k,v) in self.processor.items():
			if k == event:
				return self.processor[k](usr,key)
		else:
			return "unknown event"
	def OnSubscribe(self,usr,key):
		return self.messages["subscribe"][key]
	def OnUnsubscribe(self,usr,key):
		return self.messages["unsubscribe"][key]
	def OnClick(self,usr,key):
		return self.messages["click"][key]
	def OnLocation(self,usr,location):
		print (usr,location)
class WeixinContext:
	def __init__(self):
		self.textPlugins = {}	
		threading.Timer(1.0,self.RemoveTimeoutPlugin).start()
		self.eventPlugin = self.LoadEventPlugin()
		self.token = {"time":time.time(),"value":None}
		self.GetAccessToken()
		self.openID = ""
	def LoadEventPlugin(self):
		with open("WeixinPlugin"+os.sep+"config.xml") as f:
			xml = f.read()
			dom = etree.fromstring(xml)
			for plugin in dom:
				if plugin != None and plugin.get("target") == "event":
					f = plugin.get("class")
					if '.' in f:
						modname, clsname = f.rsplit('.', 1)
						mod = __import__(modname)
					else:
						clsname = f
						mod = sys.modules[__name__]
						
					
					cls = getattr(mod,clsname)
					clsentry = cls(self)
					
					for event in plugin:
						if event.tag == "event":
							name = event.get("name")
							if name == None:
								raise Exception("event must be assigned a name")
							if name not in clsentry.messages:
								clsentry.messages[name] = {}
							clsentry.messages[name][event.get("key")] = event.get("return")
					
					return 	clsentry	
	def LoadTextPlugin(self,usr):
		with open("WeixinPlugin"+os.sep+"config.xml") as f:
			xml = f.read()
			dom = etree.fromstring(xml)
			for plugin in dom:
				if plugin != None and plugin.get("target") == "text":
					f = plugin.get("class")
					if '.' in f:
						modname, clsname = f.rsplit('.', 1)
						mod = __import__(modname)
					else:
						clsname = f
						mod = sys.modules[__name__]
						
					
					cls = getattr(mod,clsname)
					timeout = int(plugin.get("timeoutToReset","-1"))
					return 	{'class':cls(plugin,self,usr),'timeout':timeout,"time":time.time()}	
		#return plugins
	def ProcessText(self,usr,text):
		if not usr in self.textPlugins:
			print("loadplugins")
			self.textPlugins[usr] = self.LoadTextPlugin(usr)
			#return self.usrPlugins[usr]["class"].Process(text)
		else:
			self.textPlugins[usr]["time"] = time.time()
		
		if self.textPlugins[usr] != None and self.textPlugins[usr]["class"] != None:
			return self.textPlugins[usr]["class"].Process(text)
	def ProcessEvent(self,usr,event,key):
		if self.eventPlugin != None:
			return self.eventPlugin.Process(usr,event,key)
	def RemoveTimeoutPlugin(self):
		delUser = []
		for (k,v) in self.textPlugins.iteritems():

			if v["timeout"] > 0: 
				if time.time() - v["time"] > v["timeout"]:
					#self.usrPlugins.pop(k)
					delUser.append(k)
		
		for usr in delUser:
			print('Timeout User : ' + usr)
			plugin = self.textPlugins.pop(usr)
			del plugin
		t = threading.Timer(1.0, self.RemoveTimeoutPlugin)
		t.start()
	def GetAccessToken(self):
		print(self.token)
		if self.token["value"] == None:
			self.UpdateToken()			
		if time.time() - self.token["time"] > 24*3600:
			self.UpdateToken()
		
		print(self.token["value"])
		return self.token["value"]
	def UpdateToken(self):
		opener = urllib2.build_opener(urllib2.HTTPHandler())
		url = "https://api.yixin.im/cgi-bin/token?grant_type=client_credential&appid="+ APPID +"&secret="+APPSECRET
		#req = urllib2.Request(url)
		response = opener.open(url).read()
		self.token['value'] = json.loads(response)["access_token"]
		self.token["time"] = time.time()
		
ctx = WeixinContext()				
		
class WeixinIF:
		
		def __init__(self):
			pass
		def GET(self,cmdline=""):
			wxToken = TOKEN
			data = web.input()
			if len(data) == 0:
				return 
			signature = data.signature
			timestamp = data.timestamp
			nonce = data.nonce
			echostr = data.echostr
			l = [wxToken,timestamp,nonce]
			l.sort()
			sha1 = hashlib.sha1()
			map(sha1.update,l)
			hashcode = sha1.hexdigest()
			if hashcode == signature:
				return echostr
		def POST(self,cmdline = ""):
			str_xml = web.data()
			print(str_xml)
			xml = etree.fromstring(str_xml)
			fromUser = xml.find("FromUserName").text
			toUser = xml.find("ToUserName").text
			ctx.openID = toUser
			msgType = xml.find("MsgType").text
			
			if msgType == "text":
				print(repr(xml.find("Content").text))
				return ctx.ProcessText(fromUser,xml.find("Content").text)
			elif msgType == "event":
				if xml.find("Event").text == 'LOCATION' or xml.find("Event").text == 'ENTER':
					location = {"Latitude":xml.find("Latitude").text,"Longitude":xml.find("Latitude").text,"Precision":xml.find("Precision").text}
					return ctx.ProcessEvent(fromUser,xml.find("Event").text,location)
				else:
					return ctx.ProcessEvent(fromUser,xml.find("Event").text,xml.find("EventKey").text)
	



