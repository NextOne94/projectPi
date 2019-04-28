import socket
import random

datatoserver = []
host = '192.168.137.165'
port = 5000
s = socket.socket()
s.connect((host, port))

def Main():
    
    #print(datatoserver)  
    message = input("->")
    while message != 'q':
                    randomdata()
                    sendData()
                    message = input("->")
    s.close()
    #

def randomdata():
    # for i in range(5):
    #         x = random.randint(0,23)
    #         #print(i)
    #         if len(datatoserver) == 0:
    #              datatoserver.append(x)
    #              #print(datatoserver)
    #         else :     
    #             for j in range(len(datatoserver)):
    #                 # print('len:',len(datatoserver))
    #                 # print('data J :',datatoserver[j])
    #                 # print('data X :',x)
    #                 if  x == datatoserver[j]:
    #                     x = random.randint(0,23)

    #                    # print('if :',j)
    #                     break
    #             datatoserver.append(x)

    while coun != 5:
            dup = True
            x = random.randint(0,23)
            if len(datatoserver) == 0:
                datatoserver.append(x)
                coun +=1
            else :
                for i in range(len(datatoserver)):
                    if  x == datatoserver[i]:
                        dup = False
                        break
                        
                if dup == True :
                    datatoserver.append(x)
                    coun +=1                
    print(datatoserver)

           
def sendData(*args):
    #print("AAA")

    # datatoserver.clear()
    datatoservernew ="-"
    for i in range(0, len(datatoserver), 1):
        datatoserverold = str(datatoserver[i])+'-'
        datatoservernew = datatoservernew + datatoserverold

    s.send(datatoservernew.encode('utf-8'))

    #print(datatoservernew)
    datatoserver.clear()


if __name__ == '__main__':
		#print("Server Start")
		Main()


        
