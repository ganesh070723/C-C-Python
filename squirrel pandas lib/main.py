import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

file = {

            "color": ["Black", "Gray", "Cinnamon"],
            "count": [black, gray, cinnamon]


}
filess = pandas.DataFrame(file)
filess.to_csv("squirrel.csv")
