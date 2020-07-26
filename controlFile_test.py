from time import sleep
import  sqlite3
import numpy as np
import xlsxwriter
import xlrd 


posarry = []
dAll = np.arange(0)
dAll.resize(5,5)
sumq = 0

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
            #print (row)
            name = row[1]
            locx = row[2]
            locy = row[3]
            xxx.append([name, locx, locy])
            
    
        connection.close()
    #print(xxx)
    Listtsp = TSP(xxx)#step3
    
    

def Datarecv(data): #Step1
    # datas = data.split('-')
    # datas.pop(0)
    # datas.pop(len(datas)-1)
    datas = data.tolist()
    datas.insert(0,999)
    #print(datas)
    #print(len(datas))
    select_DB(datas)#step2

def TSP(listSelects):#step3

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
        
    dall.resize(len(num1),len(num1))
    minn = dall[0][0]
    position = 0
    global  posarry 
    global sumq

    if len(posarry) > len(num1)-1: #รีเซตค่า posarry เมือเข้ารอบใหม่
        posarry = []
        sumq = 0
    for i in range(len(num1)): # คำนวนระยะห่างระหว่างจุด 2 จุด
        for j in range(len(num1)):
            xi = np.power((num1[i]-num1[j]),2)
            yi = np.power((num2[i]-num2[j]),2)
            d = np.sqrt(xi+(yi))
            dall[i][j] = d
    posarry.insert(0,0) #ล็อกตำแหน่งสุดท้าย
    print(dall)
    for i in range(len(num1)):
        #print("i =" ,i)
        minn = dall[position][position]
        point = position
        #print("point =" ,point)
        for j in range(len(num1)):
            #print("point =" ,point," j =" ,j," value j =" ,dall[point][j]," start min = ",minn )
            #print("value j =" ,dall[point][j])
            if minn == 0 :
                #print(max(dall[point]))
                minn = max(dall[point])
                #print("start min = ",minn) 
                position = j
            
                
            if minn >= dall[point][j] and dall[point][j] > 0  : #เลือกค่าที่น้อยที่สุด
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
        sumq = sumq + int(minn)
        posarry.insert(i,position)
    posarry.pop()
    print(posarry,sumq)
    pathoriginal(dall)
    print("----End----")
        
    
    return posarry


#####test on pi ######

def chackpath(x):
    
    #print(len(posarry))
    path = 0
    #print(posarry,x)
    if len(posarry) == 0 :
            path = 1
    else:        
        for i in range(len(posarry)):
            if(int(x) == int(posarry[i])):
                path = 0
                break
            else:
                path = 1
            #print("path = ",path)
    if path == 0:
        return False
    else :
        return True

def pathoriginal(dataList):
    #print(dataList)
    sumO = dataList[0][1] + dataList[1][2] + dataList[2][3] + dataList[3][4] + dataList[4][5] + dataList[5][0]
    print("path original = ", sumO) 