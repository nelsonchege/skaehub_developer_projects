import itertools as it


# define function which infinitely cylces list
def cycle_data(iterable):
    return it.cycle(iterable)


#  initiating List
list1 = ['nelson', 'issa', 'Cool', 'Dude']
result = cycle_data(list1)
print("The said function print never-ending items:")
for i in result:
    print(i)
