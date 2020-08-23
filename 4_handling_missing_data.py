import pandas as pd

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