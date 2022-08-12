import xlrd
import xlwt
import datetime
import time
from xlrd import xldate_as_tuple


wb = xlrd.open_workbook("D:/Y4/ML/China Lake.xlsx")
sheet1 = wb.sheet_by_index(5)

column = []
data = []
column.append(sheet1.cell(0,0).value)#MIDAS
column.append(sheet1.cell(0,1).value)#LAKE
column.append(sheet1.cell(0,2).value)#TOWN
column.append(sheet1.cell(0,3).value)#STATION
column.append(sheet1.cell(0,4).value)#DATE
column.append(sheet1.cell(0,5).value)#YEAR
column.append(sheet1.cell(0,6).value)#MONTH
column.append(sheet1.cell(0,7).value)#D
column.append(sheet1.cell(0,8).value)#C
column.append(sheet1.cell(0,9).value)#TIMES


for i in range(1,sheet1.nrows):#sheet1.nrows 行数
    if(sheet1.cell(i, 3).value==1 and sheet1.cell(i, 7).value==7):
        coldata=[]
        coldata.append(sheet1.cell(i, 0).value)#MIDAS
        coldata.append(sheet1.cell(i, 1).value)#LAKE
        coldata.append(sheet1.cell(i, 2).value)#TOWN
        coldata.append(sheet1.cell(i, 3).value)  #STATION
        coldata.append(sheet1.cell(i, 4).value)  # DATE
        coldata.append(sheet1.cell(i, 5).value)#YEAR
        coldata.append(sheet1.cell(i, 6).value)  #MONTH
        coldata.append(sheet1.cell(i, 7).value)  #D
        coldata.append(sheet1.cell(i, 8).value)  #C
        coldata.append(sheet1.cell(i, 9).value)  # Times
        data.append(coldata)

f = xlwt.Workbook()
sheetw1 = f.add_sheet('CHLA',cell_overwrite_ok=True)

sheetw1.write(0,0,column[0])#MIDAS
sheetw1.write(0,1,column[1])#LAKE
sheetw1.write(0,2,column[2])#TOWN
sheetw1.write(0,3,column[3])#STATION
sheetw1.write(0,4,column[4])#DATE
sheetw1.write(0,5,column[5])#YEAR
sheetw1.write(0,6,column[6])#MONTH
sheetw1.write(0,7,column[7])#D
sheetw1.write(0,8,column[8])#C
sheetw1.write(0,9,column[9])#times

i=0
while(i<len(data)):
    # print(i)
    d=data[i]
    sheetw1.write(i + 1, 0, d[0])  # 第1行第1列
    sheetw1.write(i + 1, 1, d[1])  # 第2行第1列
    sheetw1.write(i + 1, 2, d[2])  # 第3行第1列
    sheetw1.write(i + 1, 3, d[3])  # 第3行第1列
    sheetw1.write(i + 1, 5, d[5])  # 第3行第1列
    sheetw1.write(i + 1, 6, d[6])  # 第3行第1列
    sheetw1.write(i + 1, 7, d[7])  # 第3行第1列
    if(i+1<len(data)):
        dnext = data[i + 1]
        if(dnext[5]==d[5] and dnext[6]==d[6]):
            newc=d[8]+dnext[8]
            data[i][8]=newc
            data[i][9] = d[9]+1
            sheetw1.write(i + 1, 8, newc)
            sheetw1.write(i + 1, 9, d[9]+1)
            print(d[9]+1)
            print(i, data[i])
            print(i+1, data[i+1])
            del data[i+1]
        else:
            sheetw1.write(i + 1, 8, d[8])
            sheetw1.write(i + 1, 9, d[9])
            i=i+1
    else:
        sheetw1.write(i + 1, 8, d[8])
        sheetw1.write(i + 1, 9, d[9])
        i = i + 1
f.save('D:/Y4/ML/test2.xls')






