'''
Created on 2014-9-3

@author: songwensheng
'''
import WeixinIF
from lxml import etree
import sys
import os
class WxTextPlugin(WeixinIF.TextPlugin):
    def __init__(self,xml,ctx):
        WeixinIF.TextPlugin.__init__(self, xml, ctx)
        self.cnt = 0
class WxEventPlugin(WeixinIF.EventPlugin):
    def __init__(self,ctx):
        WeixinIF.EventPlugin.__init__(self, ctx)
        
    def OnSubscribe(self,usr,key):
        return "self.messages['subscribe'][key]";
    def OnUnsubscribe(self,usr,key):
        return "self.messages['unsubscribe'][key]";
    def OnClick(self,usr,key):
        return "self.messages['click'][key]";
       
class InitState(WeixinIF.State):
    def __init__(self,plugin,tips):
        WeixinIF.State.__init__(self,plugin,tips)
    def Enter(self,plugin,text):
        return "Enter  InitState"
    def Process(self,plugin,text):
        return "process in InitState"
    def Leave(self,plugin,text):
        return "Leave  InitState"

class FirstState(WeixinIF.State):
    def __init__(self,plugin,tips):
        WeixinIF.State.__init__(self,plugin,tips)
    def Enter(self,plugin,text):
        return self.tips["enter"]
    def Process(self,plugin,text):
        plugin.cnt = plugin.cnt + 1
        return str(plugin.cnt) +" In FirstState " + text       
    def Leave(self,plugin,text):
        return("leave " + self.__class__.__name__)
        
class SecondState(WeixinIF.State):
    def __init__(self,plugin,tips):
        WeixinIF.State.__init__(self,plugin,tips)
    def Enter(self,plugin,text):
        return("enter " + self.__class__.__name__)
    def Process(self,plugin,text):
        plugin.cnt = plugin.cnt + 1
        return str(plugin.cnt) +" In SecondState " + text
 
    def Leave(self,ctx,text):
        return("leave " + self.__class__.__name__)

class ThirdState(WeixinIF.State):
    def __init__(self,plugin,tips):
        WeixinIF.State.__init__(self,plugin,tips)
    def Enter(self,plugin,text):
        return("enter " + self.__class__.__name__)
    def Process(self,plugin,text):
        plugin.cnt = plugin.cnt + 1
        return str(plugin.cnt) +" In ThirdState " + text
    def Leave(self,plugin,text):
        return("leave " + self.__class__.__name__)
        
class FourthState(WeixinIF.State):
    def __init__(self,plugin,tips):
        WeixinIF.State.__init__(self,plugin,tips)
    def Enter(self,plugin,text):
        return("enter " + self.__class__.__name__)
    def Process(self,plugin,text):
        plugin.cnt = plugin.cnt + 1
        return str(plugin.cnt) +" In FourthState " + text  
    def Leave(self,plugin,text):
        return("leave " + self.__class__.__name__)