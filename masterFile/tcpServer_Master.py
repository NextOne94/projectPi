import	socket
from controlFile import *



def Main():
		host = '192.168.137.23'
		port = 5000

		s = socket.socket()
		s.bind((host,port))

		s.listen(1)
		c, addr = s.accept()
		print("Connection from: " + str(addr))
		while True :
				data = c.recv(1024).decode('utf-8')
				if not data:
						break
				print("From connection user: " + data)
				Datarecv(data)
##				select_DB(int(data))
##				print(select_DB(int(data))[0])
##				print(select_DB(int(data))[1])
				data = data.upper()
				#print("Sending: " + data)
				c.send(data.encode('utf-8'))
		c.close()

if __name__ == '__main__':
		Main()
