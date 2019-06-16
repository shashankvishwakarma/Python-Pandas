'''
https://www.hackerearth.com/practice/machine-learning/data-manipulation-visualisation-r-python/tutorial-data-manipulation-numpy-pandas-python/tutorial/
'''
import pandas as pd
import numpy as np

#load the data
train = pd.read_csv("datasets/train.csv")
test = pd.read_csv("datasets/test.csv")

#train.info() # check data set
print("The train data has",train.shape)
print("The test data has",test.shape)

#print('train head \n',train.head())
nans = train.shape[0] - train.dropna().shape[0]
print ("%d rows have missing values in the train data" %nans)

nand = test.shape[0] - test.dropna().shape[0]
print ("%d rows have missing values in the test data" %nand)

#print(train.isnull().sum()) #only 3 columns have missing values
cat = train.select_dtypes(include=['O'])
cat.apply(pd.Series.nunique)

#Education
train.workclass.value_counts(sort=True)
train.workclass.fillna('Private',inplace=True)

#Occupation
train.occupation.value_counts(sort=True)
train.occupation.fillna('Prof-specialty',inplace=True)


#Native Country
train['native.country'].value_counts(sort=True)
train['native.country'].fillna('United-States',inplace=True)
print(train.target.value_counts()/train.shape[0])


df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})

#calculate the mean of data1 column by key1
grouped = df['data1'].groupby(df['key1'])
print('calculate the mean of data1 column by key1 \n',grouped.mean())