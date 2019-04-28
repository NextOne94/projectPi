import random

datatoserver = []

def Main():
    coun = 0
    
    while coun != 5:
            dup = True
            x = random.randint(0,23)
            if len(datatoserver) == 0:
                datatoserver.append(x)
                coun +=1
            else :
                for i in range(len(datatoserver)):
                    if  x == datatoserver[i]:
                        dup = False
                        break
                        
                if dup == True :
                    datatoserver.append(x)
                    coun +=1
            

    print(datatoserver)
            

    

            

if __name__ == '__main__':
		#print("Server Start")
		Main()