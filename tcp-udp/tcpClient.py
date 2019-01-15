#TCP_CLIENT
import socket

def Main():
        host = '127.0.0.1' #กำหนดค่า host ที่เชื่อมต่อ
        port = 5000 #กำหนดค่าพอร์ตในการสื่อสาร

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #สร้าง object ในการเชื่อมต่อ socket
        s.connect((host,port)) #เชื่อมต่อ

        message = input("->")
        while message != 'q':
                        s.send(message.encode('utf-8')) #ส่งข้อมูลโดยก่อนส่งได้เข้ารหัสตัวอักษรเป็น utf-8
                        data = s.recv(1024).decode('utf-8') #แปลงข้อมูลที่ได้รับด้วยหรสอักษร utf-8
                        print("Recieved for server: " + data)
                        message = input("->")
        s.close()

if __name__ == '__main__':
        Main()
