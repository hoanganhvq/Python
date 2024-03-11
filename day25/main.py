# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#

# import csv
# with open("weather_data.csv") as data_file:
#     data  = csv.reader(data_file)
#     temparature = []
#     for row in data:
#         temparature.append(row[1])
#     print(temparature)
#     print(data)
#     for row in data:
#         print(row)

import pandas
data = pandas.read_csv("weather_data.csv")
data_list = data["temp"].to_list()
print(data["temp"].max())
# #get data in column
# print(data["temp"])
# print(data.condition)
#Get data in column

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])


#Example
# monday = data[data.day == "Monday"]
# print(monday.condition)     # It will print the conditon of monday
#
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp *9/5 + 32
# print(monday_temp_F)

#Create datafram from data of file
data_dict = {
    "student" : ["Anh","Vy"],
    "scores": [76,80]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")