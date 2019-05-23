import random
import xlsxwriter
import xlrd 
import numpy as np




# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet()





def Main():
    
    print("Select the opiton : 1: random Data ")
    print("                    2: show random data")
    select = input()
    if int(select) == 1 :
        random_data()
        Main()
    elif int(select) == 2:
        show_data()
        Main()
    elif int(select) == 0 :
        print("End")
    else:
        Main()



    
            

def random_data():
    row = 0
    
    
    for n in range(10) :
        coun = 0
        col = 0
        datatoserver = []
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
        for data in (datatoserver) :
            row = n
            worksheet.write(row, col, data)
            col += 1
    workbook.close()



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
