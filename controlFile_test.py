from time import sleep
#import RPi.GPIO as GPIO
import  sqlite3
import numpy as np
import xlsxwriter
import xlrd 


DIR_VER = 20   # Direction GPIO Pin "Vertical"
STEP_VER = 21  # Step GPIO Pin "Vertical"
DIR_HORI = 19   # Direction GPIO Pin "Horizontal"
STEP_HORI = 26  # Step GPIO Pin "Horizontal"
CW = 1     # Clockwise Rotation
CCW= 0    # Counterclockwise Rotation
SPR = 200   # Steps per Revolution (360 / 1.8)

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(DIR_VER, GPIO.OUT)
# GPIO.setup(STEP_VER, GPIO.OUT)
# GPIO.setup(DIR_HORI, GPIO.OUT)
# GPIO.setup(STEP_HORI, GPIO.OUT)

#arr = np.arange(0)
#arr.resize(16,22)
#arr1 = [(4,2),(4,14),(8,2),(12,10)]

posarry = []
dAll = np.arange(0)
dAll.resize(5,5)
#newarr = [ (0,0) ]
#x = len(arr1)






# def StepMove(xxx):#step4
#     locxold=0
#     locyold=0
    
#     for i in range(len(xxx)):
#         print("len =",len(xxx))
#         if locxold == 0 and locyold == 0 :
#             print(i ,": new")
#             locxnew = xxx[i][1]
#             locynew = xxx[i][2]
#             print(locxnew)
#             print(locynew)
#             dir_V = CCW
#             dir_H = CW
#             step_count_H = SPR * int(locxnew)*16
#             step_count_V = SPR * int(locynew)*16
#             delay = 0.007/16  # delay = Time to turn around 1 cycle / Steps ###0.25/200=0.00125
            
#             StepClk(step_count_H,step_count_V,dir_V,dir_H)
#             print(i, ": END")
#             locxold = locxnew
#             locyold = locynew
#         else :
#             print(i, ": OLD")
#             locxnew = xxx[i][1]
#             locynew = xxx[i][2]
#             print(locxnew)
#             print(locynew)
#             locxnewgo = locxnew - locxold
#             locynewgo = locynew - locyold
#             print(locxnewgo)
#             print(locynewgo)
#             if locxnewgo >= 0 :
#                 dir_H = CW
#             elif locxnewgo < 0:
#                 locxnewgo = locxnewgo * (-1)
#                 dir_H = CCW
#             if locynewgo >= 0:
#                 dir_V = CCW
#             elif locynewgo < 0:
#                 locynewgo = locynewgo * (-1)
#                 dir_V = CW
                
#             step_count_H = SPR * int(locxnewgo)*16
#             step_count_V = SPR * int(locynewgo)*16
#             delay = 0.007/16 # delay = Time to turn around 1 cycle / Steps ###0.25/200=0.00125
            
#             StepClk(step_count_H,step_count_V,dir_V,dir_H)
#             print(i,": END")
#             locxold = locxnew
#             locyold = locynew
#             if i+1 == len(xxx):
#                 dir_H = CCW
#                 dir_V = CW
#                 step_count_H = SPR * int(locxold)*16
#                 step_count_V = SPR * int(locyold)*16
#                 StepClk(step_count_H,step_count_V,dir_V,dir_H)
#                 print(i,": END Round")
    

# def StepClk(locx,locy,dir_V,dir_H):
#     print(locx)
#     print(locy)
#     delay = 0.005/16    #delay = Time to turn around 1 cycle / Steps ###0.25/200=0.00125
#     GPIO.output(DIR_VER, dir_V)
#     GPIO.output(DIR_HORI, dir_H)
#     clk_h = GPIO.HIGH
#     clk_v = GPIO.HIGH
#     status_h = False
#     status_v = False
#     while True:
#         GPIO.output(STEP_HORI, clk_h)
#         GPIO.output(STEP_VER, clk_v)
#         sleep(delay)
#         GPIO.output(STEP_HORI, GPIO.LOW)
#         GPIO.output(STEP_VER, GPIO.LOW)
#         sleep(delay)
        
#         if locx == 0 :
#             clk_h = GPIO.LOW
#             status_h = True
#         elif locx > 0:
#             locx = locx - 1
#             #print("locx =",locx)
        
#         if locy == 0 :
#             clk_v = GPIO.LOW
#             status_v = True
#         elif locy > 0 :
#             locy = locy - 1
#             #print("locy =",locy)
            
#         if status_h == True and status_v == True :
#             print("TrueTrue")
#             sleep(1)
#             break



def select_DB(datas):#step2
    xxx = []
    for i in range(len(datas)):
        data = datas[i]
        connection = sqlite3.connect('project_test.db')
        cursor = connection.cursor()
        sql_command = "SELECT * FROM medicine_data WHERE indexd = %d;" % int(data)  
        cursor.execute(sql_command)
        results = cursor.fetchall()
        for row in results:
            print (row)
            name = row[1]
            locx = row[2]
            locy = row[3]
            xxx.append([name, locx, locy])
            
    
        connection.close()
    print(xxx)
    Listtsp = TSP(xxx)#step3
    
    #StepMove(Listtsp)#step4

def Datarecv(data): #Step1
    # datas = data.split('-')
    # datas.pop(0)
    # datas.pop(len(datas)-1)
    datas = data.tolist()
    datas.insert(0,999)
    print(datas)
    print(len(datas))
    select_DB(datas)#step2

def TSP(listSelects):#step3
    #wb = xlrd.open_workbook('Expenses01.xlsx')
    #sheet = wb.sheet_by_index(1) 
    #sheet.cell_value(0, 0) 
    dall = np.arange(0)
    num1 = []
    num2 = []
    newarr = []
    
    #print("start posarry =",posarry)
    for listSelect in listSelects :
        n1 = listSelect[1]
        n2 = listSelect[2]
        newarr.append([n1, n2])
        num1.append(n1) 
        num2.append(n2)
        
    print(newarr)

    # for i in range(len(newarr)) :
    #     num1.append(newarr[i][0]) 
    #     num2.append(newarr[i][1])

    # print(num1) 
    # print(num2)
    dall.resize(len(num1),len(num1))
    minn = dall[0][0]
    position = 0
    global  posarry 

    if len(posarry) > len(num1)-1: 
        posarry = []
    for i in range(len(num1)):
        for j in range(len(num1)):
            xi = np.power((num1[i]-num1[j]),2)
            yi = np.power((num2[i]-num2[j]),2)
            d = np.sqrt(xi+(yi))
            dall[i][j] = d
    posarry.insert(len(num1)-1,0)
    print(dall) 
    for i in range(len(num1)):
        #print("i =" ,i)
        minn = dall[position][position]
        point = position
        #print("point =" ,point)
        for j in range(len(num1)):
            #print("j =" ,j)
            #print("value j =" ,dall[point][j])
            if minn == 0 :
                minn =  dall[point][j]
                #print("start min = ",minn) 
                position = j
            
                
            if minn >= dall[point][j] and dall[point][j] > 0  :
                #print(j)
                #print("Old min = ",minn)
                #print("chack_path = ",chackpath(j))
                if chackpath(j):
                   # print(j)
                    minn = dall[point][j]
                    #print("new min = ",minn)
                    position = j
                   # print("new position  = ",j)
                # if chackpath(j) == False and j == len(num1)-1 :
                #     print("not OK") 
        #print("----End LOOP J----")

        posarry.append(position)
    print(posarry)
        
    
    return posarry


#####test on pi ######

def chackpath(x):
    #print(posarry,x)
    #print(len(posarry))
    path = 0
    if len(posarry) == 0 :
            path = 1
    else:        
        for i in range(len(posarry)):
            if(x == posarry[i]):
                path = 0
                break
            else:
                path = 1
            #print("path = ",path)
    if path == 0:
        return False
    else :
        return True
