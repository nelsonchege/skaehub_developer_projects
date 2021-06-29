# Initializing list of dictionaries
lis = [{"name": "meek", "age": 30},
       {"name": "nick", "age": 26},
       {"name": "vick", "age": 19}]

# using sorted and lambda to print list sorted
# by age
print("The list printed sorting by age: ")
print(sorted(lis, key=lambda i: i['age']))
