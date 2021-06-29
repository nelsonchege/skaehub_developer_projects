# define function to get min and max
def max_min(m):
    return_max = max(m, key=lambda item: item[1])[1]
    return_min = min(m, key=lambda item: item[1])[1]
    return return_max, return_min


# Initializing list of dictionaries
students = [('V', 20), ('VI', 41), ('VII', 12), ('VIII', 78), ('IX', 77), ('X', 3)]
print(students)
print("\nMaximum and minimum values of the said list of tuples:")
# call the function
print(max_min(students))
