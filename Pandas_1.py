#pandas [series]
import numpy as np
import pandas as pd

ser = pd.Series([2,4,6,8])
print(ser)

arr_price = np.array([76.3,23.1,102.4])
arr_symbol = np.array(['FPT','ACB','VNM'])
ser = pd.Series(arr_price,index=arr_symbol)
print(ser)

#Truy xuat
print(ser["ACB"])
print(ser[2])
print(ser[1:])
print(ser[["FPT","VNM"]])
print(ser.size)
print(len(ser))
print(ser.values)
print(ser.index)
print(ser.axes)

#Truy xuat 2
dic ={'FPT':76.3,'ACD':23.1,'VNM':102.4,'AGH':7.8,'FLC':3.5,'HTC':24.2}
ser = pd.Series(dic)
print(ser)
print(ser.head(3))
print(ser.tail(2))
print(ser.mean())
print(ser.std())
print(ser.describe())

#Cap nhat
ser['FPT'] = 81
ser[2]=106
print(ser)

#Xoa phan tu
print(ser.drop(ser.index[[0,2]]))
print(ser.drop(['FLC','AGH']))
print(ser.drop(['FLC','AGH']))

#Tinh toan so hoc
print(ser + 2)
print(ser.map(lambda x:x*2))

#DataFrame
list_sample = [['PNJ',180.1,182],['VIB',22.3,21.2],['VIC',46.2,45.6],['VNM',150,146.1]]
df = pd.DataFrame(list_sample, columns = ['Symbol','Open','Close'])
print(df)

#Dataframe doc du lieu tu file .csv/.xlsx
df = pd.read_csv('employee.csv')
print(df)

df=pd.read_excel('Sales.xlsx')
print(df)

df = pd.read_csv('TCB_2018_2020.csv')
print(df)

df = pd.read_csv('TCB_2018_2020.csv', index_col=0)
print(df.head())

#Truy xuat dl theo dieu kien
df = pd.read_csv('TCB_2018_2020.csv',index_col=0)
## Xuất dữ liệu với điều kiện giá đóng cửa lớn hơn 98
print(df[df['Close']>98])

#Truy xuat du lieu theo cot
print(df[["High","Low"]].tail())
df = pd.read_csv('TCB_2018_2020.csv', header =None)
print(df[[0,2,3]].tail())

#Truy xuat du lieu theo dong
df = pd.read_csv('TCB_2018_2020.csv',index_col=0)
print(df.loc[['2019-06-10', '2020-06-10']])

df = pd.read_csv('TCB_2018_2020.csv', index_col = 0)
print(df.iloc[0])

df = pd.read_csv('TCB_2018_2020.csv',index_col=0)
print(df.iloc[[0,2]])

df = pd.read_csv('TCB_2018_2020.csv',index_col = 0)
print(df.iloc[35:41])

#Truy xuat du lieu theo phan tu
df = pd.read_csv('TCB_2018_2020.csv',index_col=0)
#Truy xuat gia dong cua ngay 20-08-2019
print(df.loc['2019-08-20','Close'])
print(df.loc['2020-12-25':,'Open'])

df = pd.read_csv('TCB_2018_2020.csv',index_col=0)
#Truy xuat dong thu 5 vaf cot dau tien
print(df.iloc[4,0])
#Truy xuat dong tu dong thu 648 voi tat ca cac cot
print(df.iloc[648:,:])