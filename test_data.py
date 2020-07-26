import random
#import xlsxwriter
#import xlrd 
import numpy as np
import  sqlite3
from controlFile_test import *
from smbus2 import SMBus
 
addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
  


# Create a workbook and add a worksheet.


index = 0





def Main():
    
    print("Select the opiton : 1: random Data ")
    print("                    2: show random data")
    print("                    3: sort and show data")
    print("                    4: Send data to stm32 with I2C protocol")
    print("                    0: To Exit")
    select = input()
    if int(select) == 1 :
        random_data()
        Main()
    elif int(select) == 2:
        show_data()
        Main()
    elif int(select) == 3:
        sort_data()
        Main()
    elif int(select) == 4:
        send_data()
        Main()
    elif int(select) == 0 :
        connection = sqlite3.connect('project_test.db')
        connection.close() 
        print("End")
    else:
        Main()

def random_data():
    connection = sqlite3.connect('project_test.db')
    cursor = connection.cursor()
    sql_command ="DELETE from dataformUser"
    cursor.execute(sql_command)
    connection.commit()
    for n in range(5) :
        coun = 0
        datafromUser = []
        while coun != 5:
                dup = True
                x = random.randint(0,23)
                if len(datafromUser) == 0:
                    datafromUser.append(x)
                    coun +=1
                else :
                    for i in range(len(datafromUser)):
                        if  x == datafromUser[i]:
                            dup = False
                            break
                                
                    if dup == True :
                        datafromUser.append(x)
                        coun +=1
                    
        #print(datafromUser)
        
        for i in range(len(datafromUser)) :
            #print(datafromUser[i])
            cursor = connection.cursor()
            sql_command = "INSERT INTO dataformUser (round, drug_id ) VALUES ( %d , %d)" %(n, int(datafromUser[i]))
            cursor.execute(sql_command)
            connection.commit()
            
    connection.close()       
        


def show_data():
    connection = sqlite3.connect('project_test.db')
    cursor = connection.cursor()
    results = [0]
    r = 0
    xxx =[]
    while(len(results) != 0):
        sql_command = "SELECT * FROM dataformUser WHERE round = %d;" % int(r)  
        cursor.execute(sql_command)
        results = cursor.fetchall()
        for row in results:
            xxx.append(row[2])   
        r=r+1
        if(len(results) != 0):
            print(xxx)
        xxx.clear()
    
    connection.close() 
    
     

def sort_data():

    connection = sqlite3.connect('project_test.db')
    cursor = connection.cursor()
    results = [0]
    r = 0
    sort = []
    while(len(results) != 0):
        sql_command = "SELECT * FROM dataformUser WHERE round = %d;" % int(r)  
        cursor.execute(sql_command)
        results = cursor.fetchall()
        for row in results:
            sort.append(row[2])   
        r=r+1
        if(len(results) != 0):
            print(sort)
            Datarecv(sort)
        sort.clear()

        
def send_data():
    
       print("444444")



if __name__ == '__main__':
		#print("Server Start")
		Main()
