import pandas as pd

df =pd.read_csv('SampleData.csv',index_col=0)
print(df)
del df['Price']
print(df)
print(df.drop(df.index[2]))
#them du lieu
df = pd.read_csv('SampleData.csv',index_col=0)
print(df)
df['Usd'] = df['Price']/23
print(df)
df =pd.read_csv('SampleData.csv')
print(df)
df.loc[df.shape[0]] = ['VCB',113.6,23.09]
print(df)

sales_2020 = pd.DataFrame({'sales':[450,360,550,480]},index=['Mar','Jun','Feb','Apr'])
print(sales_2020)
print(sales_2020.sort_index())
#sap xep du lieu
sales_2020=pd.DataFrame({'Sales': [450, 360, 550, 480]},index=['Mar', 'Jun', 'Feb', 'Apr'])
print(sales_2020)
sale_2021 = pd.DataFrame({'Sales': [650, 600, 700, 680]}, index=['Feb', 'Mar', 'Apr', 'Jun'])
print(sales_2020.reindex(sale_2021.index))

#sampleData2
df=pd.read_csv('SampleData2.csv')
print(df)
print(df.groupby('Group').sum())
#Gop du lieu
df=pd.read_csv('SampleData2.csv')
df1=df[['Symbol','Price','Group']]
df2 = df[['Symbol','PE','Group']]
print(df1)
print(df2)
df_concat = pd.concat([df1,df2])
print(df_concat)
df_concat = pd.concat([df1,df2],join='inner')
print(df_concat)
df_concat = pd.concat([df1,df2],axis=1)
print(df_concat)

df_append = df1._append(df2)
print(df_append)

df_merge = pd.merge(df1,df2)
print(df_merge)

df = pd.read_csv('SampleData2.csv')
df1 = df[['Symbol','Price','Group']]
df1 = df1.drop(df1.index[3])
df2 = df[['Symbol','PE','Group']]
print(df1)
print(df2)

df_merge = pd.merge(df1,df2)
print(df_merge)
df_merge = pd.merge(df1,df2,how='outer')
print(df_merge)
#Kiem tra du lieu rong
df = pd.read_csv('SampleData_NaN.csv')
print(df)
df=pd.read_csv('SampleData_NaN.csv')
print(df.isnull())
df = pd.read_csv('SampleData_NaN.csv')
print(df.isnull().any())

df=pd.read_csv('SampleData_NaN.csv')
print(df.isnull().sum())
print(df.isnull().sum().sum())

df = pd.read_csv('SampleData_NaN.csv')
df_delete_na_by_row = df.dropna(axis=0)
print(df_delete_na_by_row)

#Xoa gia tri
df=pd.read_csv('SampleData_NaN.csv')
df_delete_na_by_col = df.dropna(axis=1)
print(df_delete_na_by_col)

df = pd.read_csv('SampleData_NaN.csv')
df_fill_na_100 = df.fillna(100)
print(df_fill_na_100)

df = pd.read_csv('SampleData_NaN.csv')
df_fill_na_bfill = df.fillna(method='bfill')
print(df_fill_na_bfill)

df = pd.read_csv('SampleData_NaN.csv')
df_fill_na_ffill = df.fillna(method='ffill')
print(df_fill_na_ffill)

df = pd.read_csv('SampleData_NaN.csv')
df_fill_na_interpolate = df.interpolate()
print(df_fill_na_interpolate)