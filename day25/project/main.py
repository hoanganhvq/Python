import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240306.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_count)
print(red_count)
print(black_count)

data_dict = {
    "Fur_Color": ["Gray","Cinnamon","Black"],
    "Count": [gray_count, red_count, black_count]
}

df = pandas.DataFrame(data_dict) # Create the table with this data
df.to_csv("new_data.csv")