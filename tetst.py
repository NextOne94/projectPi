import numpy as np
arr = np.arange(0)

print(arr)
arr.resize(22,22)
print(arr)
#for i in range(10):
#     for j in range(10):
#         arr[i][j] = 0

print(arr)

# arr[5][9] = 500
# print(arr)


   workbook = xlsxwriter.Workbook('Expenses01.xlsx')
    worksheet = workbook.add_worksheet("RandomData")
    worksheet = workbook.add_worksheet("TSP_Data")
    row = 0
    for n in range(5) :
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
        worksheet = workbook.get_worksheet_by_name('RandomData')
        for data in (datatoserver) :
            row = n
            worksheet.write(row, col, data)
            col += 1
    workbook.close()