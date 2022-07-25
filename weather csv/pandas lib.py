import csv
import pandas
data = pandas.read_csv("weather.csv")
#temp=data["temp"].to_list()
#average = sum(temp)/len(temp)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)
temp_lis=data["temp"].to_list()

print(data[data.day=="Monday"])
print(data[data.temp == data.temp.max()])
print(data[data.temp == max(temp_lis)])

print(data.to_dict())


























































# with open("weather.csv", ) as data_file:
#     data = csv.reader(data_file)
#     tempratures = []
#     csv_list = []
#     for rows in data:
#        if rows[1] != "temp":
#            tempratures.append(int(rows[1]))
#     print(tempratures)
