import socket
import random
import numpy as np
import  sqlite3
import serial
import syslog
import time
from controlFile_test import *
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)


GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#The following line is for serial over GPIO
port = '/dev/ttyACM0'

ard = serial.Serial(port,115200,timeout=5)
time.sleep(2) # wait for Arduino

index = 0
insertData = []

countS = -1
n = 0

def my_callback(channel):  
    print ("falling edge detected on 17")  
    if len(insertData) > 0 :
        send_data()
        insertData.pop(0)
        
GPIO.add_event_detect(17, GPIO.RISING, callback=my_callback, bouncetime=300)

def Main():
    host = '192.168.137.151'
    port = 5000

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    while True :
        global countS
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("From connection user: " + data)
        print(Convert(data))
        clcDataonDB()
        saveDataDB(Convert(data))
        sort_data()
        if GPIO.input(17):
            print("radey")
            countS = countS+1
            insertData.append(countS)
            send_data()
            insertData.pop(0)

        else:
            print("Unfinish move")
            countS = countS+1
            insertData.append(countS)
        
        #print(type(data))#<class 'str'>
        #Datarecv(data)
        #data = data.upper()
    c.close()
    
def Convert(string): 
    li = list(string.split("-")) 
    return li

def clcDataonDB():
    connection = sqlite3.connect('project_test.db')
    cursor = connection.cursor()
    sql_command ="DELETE from dataformUser"
    cursor.execute(sql_command)
    connection.commit()
    connection.close()

def saveDataDB(datafromUser):
    global n
    connection = sqlite3.connect('project_test.db')
    for i in range(len(datafromUser)) :
        #print(datafromUser[i])
        cursor = connection.cursor()
        sql_command = "INSERT INTO dataformUser (round, drug_id ) VALUES ( %d , %d)" %(n, int(datafromUser[i]))
        cursor.execute(sql_command)
        connection.commit()
    n = n + 1
    connection.close()
         
def sort_data():
    connection = sqlite3.connect('project_test.db')
    cursor = connection.cursor()
    sql_command ="DELETE from data_sort"
    cursor.execute(sql_command)
    connection.commit()
    results = [0]
    r = n-1
    sort = []
    while(len(results) != 0):
        sql_command = "SELECT * FROM dataformUser WHERE round = %d;" % int(r)  
        cursor.execute(sql_command)
        results = cursor.fetchall()
        print(results)
        for row in results:
            sort.append(row[2])   
        r=r+1
        if(len(results) != 0):
            print(sort)
            Datarecv(sort)
        sort.clear()
        
    connection.close()
       
def send_data():
    r = insertData[0]
    print(r)
    sorts = ""
    connection = sqlite3.connect('project_test.db')
    cursor = connection.cursor()
    sql_command = "SELECT locX, locY FROM data_sort WHERE round = %d;" % int(r)  
    cursor.execute(sql_command)
    results = cursor.fetchall()
    for row in results:
        sorts = sorts + str(row[0]*3600)
        sorts = sorts + '-'
        sorts = sorts + str(row[1]*500)
        sorts = sorts + '-'
        #sorts.append(str(row[0]*3600))
        #print("row[0] :",row[0])
        #sorts.append(str(row[1]*500))
        #print("row[1] :",row[1]*10000)
    #sort = list(sum(sort,()))
    print(sorts)
    ard.write(sorts.encode("utf-8"))
    #for sort in sorts :
        #print("sort : ",sort)
        #ard.write(sort.encode("utf-8"))
        #time.sleep(1)

    #sorts.clear()


if __name__ == '__main__':
        print("Server Start")
        Main()

