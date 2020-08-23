import pandas as pd

df = pd.read_csv("datasets/stock_data.csv")
print(df)

df = pd.read_csv("datasets/stock_data.csv", skiprows=1)  # skip 1st row
print(df)

df = pd.read_csv("datasets/stock_data.csv", header=1)  # skip 1st row
print(df)

df = pd.read_csv("datasets/stock_data.csv", header=None, names=["ticker", "eps", "revenue", "people"])
print(df)

df = pd.read_csv("datasets/stock_data.csv", na_values=["n.a.", "not available"])
print(df)

df = pd.read_csv("datasets/stock_data.csv", na_values={
    'eps': ['not available'],
    'revenue': [-1],
    'people': ['not available', 'n.a.']
})
print(df)

df.to_csv("new.csv")  # by default it will write index as well

df.to_csv("new.csv", index=False) # by default it will write index as well
