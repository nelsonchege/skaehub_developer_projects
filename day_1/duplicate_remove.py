# creating the list
list1 = [15, 9, 5,"a", 3,"a", 5,"b","c", 6, 1]
# using str() to convert list to string data type
print ("The original list is : " + str(list1))
# using set() to remove duplicated from list
list2 = list(set(list1))
# printing list after removing the duplicates
print ("The list after removing duplicates : " + str(list2))