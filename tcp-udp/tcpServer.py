#TCP_SERVER
import	socket

def Main():
		host = '127.0.0.1' #กำหนดค่า host ที่เชื่อมต่อ
		port = 5000 #กำหนดค่าพอร์ตในการสื่อสาร

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #สร้าง object ในการเชื่อมต่อ socket
		s.bind((host,port)) #เชื่อมต่อ

		s.listen(1) #จำนวนสูงสุดของการเชื่อมต่อคิวที่เราจะอนุญาต
		c, addr = s.accept()  #รับข้อมูลการเชื่อมต่อขาเข้า
		print("Connection from: " + str(addr))
		while True :
				data = c.recv(1024).decode('utf-8')  #แปลงข้อมูลที่ได้รับด้วยรหัสอักษร utf-8
				if not data:
						break
				print("From connection user: " + data)
				data = data.upper()
				print("Sending: " + data)
				c.send(data.encode('utf-8')) #ส่งข้อมูลกับไปหาต้นทาง
		c.close()

if __name__ == '__main__':
		Main()