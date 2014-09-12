'''
Created on 2014-9-3

@author: songwensheng
'''
import WeixinIF
from lxml import etree
import sys
import os
import web
import time
import tts
class WxTextPlugin(WeixinIF.TextPlugin):
    def __init__(self,xml,ctx,usr):
        WeixinIF.TextPlugin.__init__(self, xml, ctx)
        self.FromUser = usr
        self.ToUser = ctx.openID
        self.render = web.template.render('WeixinPlugin/templates')
        
       
class InitState(WeixinIF.State):
    def __init__(self,plugin,tips):
        WeixinIF.State.__init__(self,plugin,tips)
    def Enter(self,plugin,text):
        return plugin.render.reply_InitState(plugin,"enter "+text,int(time.time()))
    def Process(self,plugin,text):
        return plugin.render.reply_InitState(plugin,text,int(time.time()))
    def Leave(self,plugin,text):
        return plugin.render.reply_InitState(plugin,"leave "+text,int(time.time()))

class TTSState(WeixinIF.State):
    def __init__(self,plugin,tips):
        WeixinIF.State.__init__(self,plugin,tips)
    def Enter(self,plugin,text):
        return plugin.render.reply_FirstState(plugin,"enter "+text + " Mode",int(time.time()))
    def Process(self,plugin,text):
        file = tts.GetAac(text)
        #xml = plugin.render.reply_TTS(plugin,text,"http://mc.faithsws.com/aac/"+file,int(time.time())) 
	#print(xml)
	#return xml
        return plugin.render.reply_FirstState(plugin,file,int(time.time()))
    def Leave(self,plugin,text):
        return plugin.render.reply_FirstState(plugin,"leave "+text,int(time.time()))
        
class SecondState(WeixinIF.State):
    def __init__(self,plugin,tips):
        WeixinIF.State.__init__(self,plugin,tips)
    def Enter(self,plugin,text):
        return plugin.render.reply_SecondState(plugin,"enter "+text,int(time.time()))
    def Process(self,plugin,text):
        return plugin.render.reply_SecondState(plugin,text,int(time.time()))
 
    def Leave(self,plugin,text):
        return plugin.render.reply_SecondState(plugin,"leave "+text,int(time.time()))

class ThirdState(WeixinIF.State):
    def __init__(self,plugin,tips):
        WeixinIF.State.__init__(self,plugin,tips)
    def Enter(self,plugin,text):
        return plugin.render.reply_ThirdState(plugin,"enter "+text,int(time.time()))
    def Process(self,plugin,text):
        return plugin.render.reply_ThirdState(plugin,text,int(time.time()))
    def Leave(self,plugin,text):
        return plugin.render.reply_ThirdState(plugin,"leave "+text,int(time.time()))
        
class FourthState(WeixinIF.State):
    def __init__(self,plugin,tips):
        WeixinIF.State.__init__(self,plugin,tips)
    def Enter(self,plugin,text):
        return plugin.render.reply_FourthState(plugin,"enter "+text,int(time.time()))
    def Process(self,plugin,text):
        return plugin.render.reply_FourthState(plugin,text,int(time.time()))
    def Leave(self,plugin,text):
        return plugin.render.reply_FourthState(plugin,"leave "+text,int(time.time()))
    
class WxEventPlugin(WeixinIF.EventPlugin):
    def __init__(self,ctx):
        WeixinIF.EventPlugin.__init__(self, ctx)
        
    def OnSubscribe(self,usr,key):
        return "self.messages['subscribe'][key]";
    def OnUnsubscribe(self,usr,key):
        return "self.messages['unsubscribe'][key]";
    def OnClick(self,usr,key):
        return "self.messages['click'][key]";
