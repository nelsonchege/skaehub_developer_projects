import pandas as pd
import random
import string


# task one
def check_leap_years(year):
    # set a boolean value of false to leap year
    leap = False
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                leap = True
    # in the if statement if the argument is not true the value of leap will not change to true
    return leap


# task two
def csv_as_dict(csv_file):
    # use the pandas to read the csv as dictionary
    csv_data = pd.read_csv(csv_file, header=None, dtype={0: str}).set_index(0).squeeze().to_dict()
    return csv_data


# task three
def remove_duplicates(my_list):
    # convert it to set because sets only display unique items
    my_set = set(my_list)
    return list(my_set)


# task four

def get_password(ranged):
    # get random password pf length 8 with letters, digits, and symbols
    # string.ascii_letters: To include letters from a-z and A-Z
    # string.digits: To include digits from 1 to 10
    # string.punctuation: to get special symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    # range argument is for the length of the password
    password = ''.join(random.choice(characters) for i in range(ranged))
    return password


# task five
def word_length(word_e):
    # Split a string into a list using .split()
    word = word_e.split()
    # when running this function it will return the length of the word
    return len(word[-1])
