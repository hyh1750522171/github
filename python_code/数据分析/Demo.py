import pandas as pd
import matplotlib as mb

if __name__ == '__main__':

    data = pd.read_excel('./数据/学生医保信息表.xlsx')
    data1 = pd.read_excel("./数据/data.xlsx")
    data2 = pd.ExcelFile("./数据/data.xlsx")
    data5 = pd.read_excel("./数据/云算3181班10月份学生kpi月度量化考核结果.xlsx")
    # data3 = pd.DataFrame(data2)
    # data3 = mb.checkdep_dvipng()
    # for i in data2:
    #     print(i)
    # print(data1)
    t = True
    f = False