import pandas as pd

XYZ_web = {
        'Day': [1, 2, 3, 4, 5, 6], "Visitors": [1000, 700, 6000, 1000, 400, 350],
        "Bounce_Rate": [20, 20, 23, 15, 10, 34]
    }
df = pd.DataFrame(XYZ_web)
print(df)

print(' ----------- Slicing the Data Frame ------------')
print('head 2 \n', df.head(2))
print('tail 2 \n', df.tail(2))

print(' ----------- Merge Operation ------------')
df1 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]},
                   index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]},
                   index=[2005, 2006, 2007, 2008])

merged = pd.merge(df1, df2)
print('Merging df1 and df2 \n',merged)

merged= pd.merge(df1,df2,on ="HPI")
print('Merge df1 and df2 on column \n', merged)

print(' ----------- Join Operation ------------')
'''
Joining - 
It is yet another convenient method to combine two differently indexed data frames into a single result data frame. 
This is quite similar to the “merge” operation, except the joining operation will be on the “index” instead of  the “columns”.
'''
df1 = pd.DataFrame({"Int_Rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({"Low_Tier_HPI": [50, 45, 67, 34], "Unemployment": [1, 3, 5, 6]}, index=[2001, 2003, 2004, 2004])

joined = df1.join(df2)
print('Join Operation \n',joined)
'''
Note - As you can notice in the above output, in year 2002(index), 
there is no value attached to columns “low_tier_HPI” and “unemployment”, therefore it has printed NaN (Not a Number). 
Later in 2004, both the values are available, therefore it has printed the respective values.
'''

print(' ----------- concat operation ------------')

'''
Concatenation -
basically glues the data frames together. You can select the dimension on which you want to concatenate. 
'''

df1 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]},
                   index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]},
                   index=[2005, 2006, 2007, 2008])

concat = pd.concat([df1, df2])
print('concat operation \n',concat)

concat = pd.concat([df1, df2], axis=1)
print('concat operation on axis 1 \n',concat)

print(' ----------- Change index to column ------------')
df = pd.DataFrame({"Day": [1, 2, 3, 4], "Visitors": [200, 100, 230, 300], "Bounce_Rate": [20, 45, 60, 10]})
df.set_index("Day", inplace=True)
print('Change the index to column \n',df)

print(' ----------- Change column name ------------')
df = pd.DataFrame({"Day": [1, 2, 3, 4], "Visitors": [200, 100, 230, 300], "Bounce_Rate": [20, 45, 60, 10]})
df = df.rename(columns={"Visitors": "Users"})
print('Change column name \n',df)

print(' ----------- data frame describe ------------')
data = pd.DataFrame({'Country': ['Russia','Colombia','Chile','Equador','Nigeria'],
                    'Rank':[121,40,100,130,11]})
print('describe data frame \n',data.describe())

print(' ----------- data frame sort ------------')
data = pd.DataFrame({'group':['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],'ounces':[4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data.sort_values(by=['ounces'],ascending=True,inplace=False)) # inplace false will not make changes to data frame
data.sort_values(by=['group','ounces'],ascending=[True,False],inplace=False)
#print('data after sort \n',data) # will not be affected by sort as inplace is False

#create another data with duplicated rows
data = pd.DataFrame({'k1':['one']*3 + ['two']*4, 'k2':[3,2,1,3,3,4,4]})
print('data frame after dropping duplicate \n',data.drop_duplicates())
print('data frame after dropping duplicate with subset K1 \n',data.drop_duplicates(subset='k1'))
