import numpy as np

# create an empty list
lst = []
# this will be the number of elements that the user wants in the array
n = int(input("Enter number of elements you want in the list : "))
# the number of elements should not be less than five
if n < 5:
    print("elements should be more than 5 elements")
    n = int(input("Enter number of elements you want in the list : "))
# a for loop to loop throw the number of elements wanted in the array
for i in range(0, n):
    ele = int(input())
    # this appends the element to the end of the list
    lst.append(ele)
print("your list is:")
print(lst)
# converts the list to a numpy array
get_size = np.array(lst)
print("Size of the memory occupied by the said array:")
print("%d bytes" % (get_size.size * get_size.itemsize))
