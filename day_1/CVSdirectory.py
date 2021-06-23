import csv
# .DictReader reads throw the csv file
data = csv.DictReader(open("schools.csv"))
print("CSV file as a dictionary:\n")
# the forloop is used to keep data to its own row
for row in data:
    print(row)