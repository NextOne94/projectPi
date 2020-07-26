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
    print("                    3: show sort data")
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
                    
        print(datafromUser)
        
        for i in range(len(datafromUser)) :
            print(datafromUser[i])
            cursor = connection.cursor()
            sql_command = "INSERT INTO dataformUser (round, drug_id ) VALUES ( %d , %d)" %(n, int(datafromUser[i]))
            cursor.execute(sql_command)
            connection.commit()
            
    connection.close()       
        


def show_data():
    wb = xlrd.open_workbook('Expenses01.xlsx')
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0) 

    # print(sheet.nrows)
    # print(sheet.ncols)
    data = np.arange(0)
    data.resize(sheet.nrows,sheet.ncols)

    #print(data)
    for i in range(sheet.nrows):
        for j in range(sheet.ncols):
            data[i][j] = sheet.cell_value(i,j)
    

    print(data)
     

def sort_data():

    wb = xlrd.open_workbook('Expenses01.xlsx')
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0) 
    data = np.arange(0)
    data.resize(sheet.nrows,sheet.ncols)

   
    for i in range(sheet.nrows):
        for j in range(sheet.ncols):
            data[i][j] = sheet.cell_value(i,j)
    print(data[0])
    for i in range(len(data)):
        Datarecv(data[i])
        
def send_data():
    
       print("444444")



if __name__ == '__main__':
		#print("Server Start")
		Main()
