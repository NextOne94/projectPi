#UDP_SERVER
import	socket

def Main():
		host = '127.0.0.1' #กำหนดค่า host ที่เชื่อมต่อ
		port = 5000 #กำหนดค่าพอร์ตในการสื่อสาร

		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #สร้าง object ในการเชื่อมต่อ socket
		s.bind((host,port)) #เชื่อมต่อ

		print("Server Started")
		while True: 
				c, addr = s.recvfrom(1024)  #ดึงผลลัพธ์การส่งข้อมูล
				data = c.decode('utf-8') #แปลงข้อมูลที่ได้รับด้วยรหัสอักษร utf-8
				print("Message From :" + str(addr))
				print("From connected user: " + data)
				data = data.upper()
				print("Sending: " + data)
				s.sendto(data.encode('utf-8'), addr) #ส่งข้อมูลกับไปหาต้นทาง
		c.close()
if __name__ == '__main__':
		Main()
