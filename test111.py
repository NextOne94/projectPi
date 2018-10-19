import numpy as np
arr = np.arange(0)
arr.resize(16,22)
arr1 = [(4,2),(4,14),(8,2),(12,10)]
num1 = []
num2 = []
dall = []
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

for i in range(len(num1)-1):
        xi = np.power((num1[0]-num1[i+1]),2)
        yi = np.power((num2[0]-num2[i+1]),2)
        d = np.sqrt(xi+(yi))
        dall.append(d)
minn = dall[0]
position = 0
for i in range(len(dall)):
       if (minn > dall[i]):
        minn = dall[i]
        position = i
        

print(dall)
print(position)



for i in range(len(num1)):
        for j in range(len(num1)):
                xi = np.power((num1[i]-num1[j]),2)
                yi = np.power((num2[i]-num2[j]),2)
                d = np.sqrt(xi+(yi))
                dAll[i][j] = d         


