import web

class WebLogin:
		def __init__(self):
				pass
		def GET(self):
				print(web.input())
				web.ctx['s'] = 1
				return "123"
