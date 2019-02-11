#UDP_CLIENT
import	socket

def Main():
		host = '192.168.43.154'  #กำหนดค่า host ที่เชื่อมต่อ
		port = 5000 #กำหนดค่าพอร์ตในการสื่อสาร

		server = (host, port) #รวม host กับค่าพอร์ตเข้าเป็น tuple เดียวกัน

		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #สร้าง object ในการเชื่อมต่อ socket
		s.connect(server) #เชื่อมต่อ

		massage = input("->")
		while massage != 'q':
				s.sendto(massage.encode('utf-8'), server)  #ส่งข้อมูลโดยก่อนส่งได้เข้ารหัสตัวอักษรเป็น utf-8
				data, addr = s.recvfrom(1024)  #ดึงผลลัพธ์การส่งข้อมูล
				data = data.decode('utf-8') #แปลงข้อมูลที่ได้รับด้วยหรสอักษร utf-8
				print("Recieved form server: " + data)
				massage = input("->")
				
		s.close()
if __name__ == '__main__':
		Main()
