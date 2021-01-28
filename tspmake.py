from time import sleep
import  sqlite3
import numpy as np

rud = 0
sumq = 0
posarry = []
completed = []
n = 0
int(cost) = 0

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
    
    
    
    TSP(xxx)#step3


def Datarecv(data): #Step1
    data.insert(0,999)
    select_DB(data)#step2


def TSP(listSelects):#step3
    global ary 
    global cost
    ary = np.arange(0)
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
        
    ary.resize(len(num1),len(num1))
    minn = ary[0][0]
    position = 0
    
    global posarry 
    global sumq
    global rud
    

    if len(posarry) > len(num1)-1: #รีเซตค่า posarry เมื่อเข้ารอบใหม่
        posarry = []
        sumq = 0
    for i in range(len(num1)): # คำนวนระยะห่างระหว่างจุด 2 จุด
        for j in range(len(num1)):
            xi = np.power((num1[i]-num1[j]),2)
            yi = np.power((num2[i]-num2[j]),2)
            d = np.sqrt(xi+(yi))
            ary[i][j] = d 
    mincost(0)
    print("  Minimum cost is %d ", cost)



def mincost (city):
    i =ncity = 0
    completed[city] = 1
    print("%d --->",city +1)
    ncity = least(city)
    if (ncity == 99):
        ncity = 0
        print("%d",ncity +1)
        cost += ary[city][ncity]
        return
    mincost(ncity)
def least(c):
    nc = 999
    min = 999
    
    for i in range(n):
       if (ary[c][i]!=0 and completed[i] == 0):
           if(ary[c][i] + ary[i][c] < min ):
               min = ary[i][0] + ary[c][i]
               kmin = ary[c][i]
               nc = i
    if(min != 999):
        cost += kmin
    return nc

