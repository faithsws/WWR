'''
Created on 2014-9-5

@author: songwensheng
'''
import web

class WebLogin:
    def GET(self):
        return "weblogin"

class WebLogout:    
    def GET(self):
        return "weblogout"