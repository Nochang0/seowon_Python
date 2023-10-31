# 7과 6번

colors = ["red", "green", "blue"]
values = ["#FF0000", "#008000", "#0000FF"]

result = {}

for index, color in enumerate(colors):
    result[color] = values[index]

print(result)