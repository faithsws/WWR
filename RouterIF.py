import socket
import Utils
import threading
import time
class Connection(threading.Thread):
	def __init__(self,conn,addr,parent):
		threading.Thread.__init__(self)
		self.conn = conn
		self.addr = addr
		self.parent = parent
		self.mac = ""
		self.info = ""
		pass
	def run(self):
		#self.conn.settimeout(5)
		#self.file = self.conn.makefile
		while True:
			try:
				buf = self.conn.recv(65524)
				if len(buf) == 0:
					raise Exception("socket failed")
				print(buf)
			except Exception,ex:
				print(ex)
				self.parent.RemoveConnection(self)
				return
			
			

class RouteIF:
		def __init__(self):
			self.connections = []
		def RemoveConnection(self,conn):
			self.connections.remove(conn)
		def StartServer(self):
			th = threading.Thread(target=self.Server)
			th.start()
			while True:
				time.sleep(1)
				print(len(self.connections))
		def Server(self):
			sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			sock.bind(("0.0.0.0",Utils.PluginConfig['RouteIF']['port']))
			sock.listen(Utils.PluginConfig['RouteIF']['maxConnections'])
			try:
				while True:
					connection,address = sock.accept()
					conn = Connection(connection,address,self)
					
					self.connections.append(conn)
					conn.start()
					
					
			except Exception,ex:
				print(ex)
				
					