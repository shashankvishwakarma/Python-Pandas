import pandas as pd
import numpy as np

df = pd.read_csv("datasets/weather_data_with_missing_data.csv", parse_dates=["day"])
print(type(df.day[0]))  # parsing day to date
df.set_index('day', inplace=True)
print(df)

# replace Nan with '0'
new_df = df.fillna(0)
print(new_df)

# passing dictionary to set value individually for col
new_df = df.fillna({
    "temperature": 0,
    "windspeed": 0,
    "event": "no event"
})
print(new_df)

# fill NaN value with previous value i.e carry forward previous value
new_df = df.fillna(method="ffill")
print(new_df)

# by default it will do linear interpolation to cal value
new_df = df.interpolate()
print(new_df)

new_df = df.interpolate(method="time")
print(new_df)

# drop if at least one col is na
new_df = df.dropna(how="all")
print(new_df)

# drop if all col is na
new_df = df.dropna(how="all")
print(new_df)

# do not drop if at least one value is not na
new_df = df.dropna(thresh=1)
print(new_df)

date_range = pd.date_range("01-01-2017", "01-11-2017")
idx = pd.DatetimeIndex(date_range)
new_df = df.reindex(idx)
print(new_df)

# Replacing list with single value
new_df = df.replace([-99999, -88888], np.NaN)
print(new_df)

# Replacing per column
new_df = df.replace({
    "temperature": -99999,
    "windspeed": -88888,
    "event": "0"
}, np.NaN)
print(new_df)

# regex - when windspeed is 6 mph, 7 mph etc. & temperature is 32 F, 28 F etc.
new_df = df.replace({'temperature': '[A-Za-z]', 'windspeed': '[a-z]'}, '', regex=True)
print(new_df)

# Replacing by using mapping
new_df = df.replace({
    -99999: np.nan,
    'no event': 'Sunny',
})
print(new_df)

df = pd.DataFrame({
    'score': ['exceptional', 'average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})
print(df)

# Replacing list with another list
df = df.replace(['poor', 'average', 'good', 'exceptional'], [1, 2, 3, 4])
print(df)
