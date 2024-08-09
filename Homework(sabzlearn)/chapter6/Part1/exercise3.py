my_list = [{"name": "apple", "weight": 50, "color": "red"},
           {"name": "banana", "weight": 60, "color": "yellow"},
           {"name": "orange", "weight": 55, "color": "orange"}]

my_list.sort(key = lambda x: x["color"])
print(my_list)