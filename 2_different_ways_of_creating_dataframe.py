import pandas as pd

df = pd.read_csv("datasets/weather_data.csv")
print(df)

# df = pd.read_excel("datasets/weather_data.xlsx", 'Sheet1')
# print(df)

# using dictionary
weather_data = {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017'],
    'temperature': [32, 35, 28],
    'windspeed': [6, 7, 2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df = pd.DataFrame(weather_data)
print("using dictionary: =====================\n", df)

# using tuple
weather_data = [
    ('1/1/2017', 32, 6, 'Rain'),
    ('1/2/2017', 35, 7, 'Sunny'),
    ('1/3/2017', 28, 2, 'Snow')
]
df = pd.DataFrame(weather_data, columns=["day", "temperature", "windspeed", "event"])
print("using tuple: =====================\n", df)


# Using list of dictionary
weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},

]
df = pd.DataFrame(weather_data)
print("using list: =====================\n", df)
