import random

datatoserver = []

def Main():
    coun = 0
    datatoserver.insert(5,111)
    print(datatoserver)
    # while coun != 5:
    #         dup = True
    #         x = random.randint(0,23)
    #         if len(datatoserver) == 0:
    #             datatoserver.append(x)
    #             coun +=1
    #         else :
    #             for i in range(len(datatoserver)):
    #                 if  x == datatoserver[i]:
    #                     dup = False
    #                     break
                        
    #             if dup == True :
    #                 datatoserver.append(x)
    #                 coun +=1
    
    for i in range(10):
        print(i)
        datatoserver.insert(i,i)


    print(datatoserver)
            
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
    

            

if __name__ == '__main__':
		#print("Server Start")
		Main()