# create a function that takes an argument of a year
def check_leap_year(year):
    # set a boolean value of false to leap year
    leap = False
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                leap = True
    # in the if statement if the argument is not true the value of leap will not change to true
    return leap
# call the check_leap_year() to execute the function
year = check_leap_year(int(input("Please enter a year: ")))

print(year)