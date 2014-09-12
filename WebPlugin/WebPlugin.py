'''
Created on 2014-9-5

@author: songwensheng
'''
import web
import os
class WebLogin:
    def GET(self):
        return "weblogin"

class WebLogout:    
    def GET(self):
        return "weblogout"
    
class WebDownloadAac:
    def GET(self,name):
        if name in os.listdir("tts"):
            return open('tts'+ os.sep + name).read()
        else:
            return "no aac"