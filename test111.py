import numpy as np
arr = np.arange(0)
arr.resize(16,22)
arr1 = [(4,2),(4,14),(8,2),(12,10)]
num1 = []
num2 = []
dall = np.arange(0)
dall.resize(5,5)
dAll = np.arange(0)
dAll.resize(5,5)
newarr = [ (0,0) ]
x = len(arr1)

for i in range(x) :
        newarr.append(arr1[i])
print(newarr)
for i in range(len(newarr)) :
        num1.append(newarr[i][0]) 
        num2.append(newarr[i][1])

print(num1) 
print(num2)

position = 0
for i in range(len(num1)):
        xi = np.power((num1[position]-num1[i]),2)
        yi = np.power((num2[position]-num2[i]),2)
        d = np.sqrt(xi+(yi))
        dall[position][i] = d
        minn = dall[position][position]
        for j in range(len(num1)):
        if minn == 0 :
                minn =  dall[position][j]
                position = i
       
        if minn > dall[i][j] and dall[i][j] > 0 :
                minn = dall[i]
                position = i




for i in range(len(num1)):
        xi = np.power((num1[0]-num1[i]),2)
        yi = np.power((num2[0]-num2[i]),2)
        d = np.sqrt(xi+(yi))
        dall[0][i] = d
print(dall)
minn = dall[0][0]
position = 0
for i in range(len(num1)):
        if minn == 0 :
                minn =  dall[0][i]
                position = i
       
        if minn > dall[0][0] and dall[0][0] > 0 :
                minn = dall[i]
                position = i

print(dall)
print(position)

for i in range(len(num1)):
        xi = np.power((num1[position]-num1[i]),2)
        yi = np.power((num2[position]-num2[i]),2)
        d = np.sqrt(xi+(yi))
        dall[1][i] = d
        


print(dall)

for i in range(len(num1)):
        for j in range(len(num1)):
                xi = np.power((num1[i]-num1[j]),2)
                yi = np.power((num2[i]-num2[j]),2)
                d = np.sqrt(xi+(yi))
                dAll[i][j] = d         
####
