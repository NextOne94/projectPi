import numpy as np
arr = np.arange(0)
arr.resize(16,22)
arr1 = [(4,2),(4,14),(8,2),(12,10)]
num1 = []
num2 = []
dAll = np.arange(0)
dAll.resize(4,4)



x = len(arr1)

for i in range(x) :
        num1.append(arr1[i][0]) 
        num2.append(arr1[i][1])

print(num1) 
print(num2)


for i in range(len(num1)):
        for j in range(len(num1)):
                xi = np.power((num1[i]-num1[j]),2)
                yi = np.power((num2[i]-num2[j]),2)
                d = np.sqrt(xi+(yi))
                dAll[i][j] = d         

print(dAll)