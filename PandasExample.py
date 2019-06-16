# Import modules
import pandas as pd

# Set ipython's max row display
pd.set_option('display.max_row', 10)

# Set iPython's max column width to 50
pd.set_option('display.max_columns', 10)

# Create an example dataframe
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'year': [2012, 2012, 2013, 2014, 2014],
        'reports': [4, 24, 31, 2, 3]}

df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
#df = pd.DataFrame(data)
index = df.index
columns = df.columns
values = df.values
#print(df)

#Selecting a single column as a Series
print(df['name'])

#Selecting a multiple column as a Series
print(df[['name','year']])

#Select a single row as a Series with .loc
print(df.loc['Pima'])

#Select multiple rows as a DataFrame with .loc
print(df.loc[['Pima','Santa Cruz']])

#Use slice notation to select a range of rows with .loc
print(df.loc['Pima':'Maricopa'])

#Select two rows and three columns
print(df.loc[['Pima','Santa Cruz'],['name','year','reports']])

#Selecting all of the rows and some columns
print(df.loc[:,['year','reports']])

#Selecting a single row with .iloc - index starts from 0 here
print(df.iloc[[3,2,4]])

#Use slice notation to select a range of rows with .iloc
print(df.iloc[3:5])

#Use comparison operator with a single column of data
criteria = df.year >= 2013
#print(criteria.head(10))

df_year_2013_or_more = df[criteria]
print(df_year_2013_or_more.head())

#Boolean selection in one line
print(df[(df['year'] >= 2013) & (df.name == 'Tina')].head())

#Combining isin with other criteria
print(df[df.year.isin([2013,2014])].head())
print(df[df.name.isin(['Tina','Amy'])].head())



