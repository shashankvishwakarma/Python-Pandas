import pandas as pd

df = pd.read_csv("datasets/weather_data.csv")
rows, columns = df.shape
print(rows)
print(columns)

print(df.head(2))
print(df[2:5])

print(df.columns)
print(df.event)

print(df[["event", "day"]])

# printing stats for data frame
print("Maximum temperature", df["temperature"].max())
print("Minimum temperature", df["temperature"].min())
print("Standard deviation temperature", df["temperature"].std())

print(df.describe())

# conditionally selecting data
print(df[df["temperature"] >= 32])
print(df[["day", "temperature"]][df.temperature == df.temperature.max()])

print(df.index)
df.set_index("day", inplace=True)
print(df)

print("loc: ", df.loc['1/3/2017'])

df.reset_index(inplace=True)
print(df)

df.set_index("event", inplace=True)
print("loc: ", df.loc['Snow'])
