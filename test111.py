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
posarry = [0]





def Main():
        for i in range(x) :
                newarr.append(arr1[i])
        print(newarr)
        for i in range(len(newarr)) :
                num1.append(newarr[i][0]) 
                num2.append(newarr[i][1])

        print(num1) 
        print(num2)
        minn = dall[0][0]
        position = 0
        
        for i in range(len(num1)):
                for j in range(len(num1)):
                        xi = np.power((num1[i]-num1[j]),2)
                        yi = np.power((num2[i]-num2[j]),2)
                        d = np.sqrt(xi+(yi))
                        dall[i][j] = d

        print(dall) 
        for i in range(len(num1)):
                minn = dall[position][position]
                point = position
                for j in range(len(num1)):
                        if minn == 0 :
                                minn =  dall[point][j]
                                position = j
                
                        if minn >= dall[point][j] and dall[point][j] > 0  :
                                if chackpath(j):
                                        minn = dall[point][j]
                                        position = j
                posarry.append(position)
        
        print(posarry) 






def chackpath(x):
        path = 0
        for i in range(len(posarry)):
                if(x == posarry[i]):
                       path = 0
                       break
                else:
                        path = 1
        if path == 0:
                return False
        else :
                return True









if __name__ == '__main__':
		print("tsp")
		Main()










#for i in range(len(num1)):
 #       xi = np.power((num1[0]-num1[i]),2)
 #       yi = np.power((num2[0]-num2[i]),2)
  #      d = np.sqrt(xi+(yi))
 #       dall[0][i] = d
#print(dall)
#minn = dall[0][0]
#position = 0
#for i in range(len(num1)):
#        if minn == 0 :
#                minn =  dall[0][i]
  #              position = i
  #     
   #     if minn > dall[0][0] and dall[0][0] > 0 :
  #              minn = dall[i]
    #            position = i

#print(dall)
#print(position)

#for i in range(len(num1)):
 #       xi = np.power((num1[position]-num1[i]),2)
 #       yi = np.power((num2[position]-num2[i]),2)
 #       d = np.sqrt(xi+(yi))
 #       dall[1][i] = d
        


#print(dall)

#for i in range(len(num1)):
#        for j in range(len(num1)):
#                xi = np.power((num1[i]-num1[j]),2)
#                yi = np.power((num2[i]-num2[j]),2)
 #               d = np.sqrt(xi+(yi))
#                dAll[i][j] = d         
####
