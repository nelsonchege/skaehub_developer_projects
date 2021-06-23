import random
import string


# defining the main method
def main():
    # select variable is used to get the strength of the password wanted which has four options
    selected_option = int(input("Please enter the password difficulty level:"
                                " \n 1. Easy \n 2. Medium \n 3.Hard "
                                " \n 4. Very Hard \n "))
    while selected_option < 1 or selected_option > 4:
        selected_option = int(input("Please enter the password difficulty level between 1 and 4:"
                                    " \n 1. Easy \n 2. Medium \n 3.Hard "
                                    " \n 4. Very Hard \n "))

    # defining a fuction that generate the password
    def get_password(ranged):
        # get random password pf length 8 with letters, digits, and symbols
        # string.ascii_letters: To include letters from a-z and A-Z
        # string.digits: To include digits from 1 to 10
        # string.punctuation: to get special symbols
        characters = string.ascii_letters + string.digits + string.punctuation
        # range argument is for the length of the password
        password = ''.join(random.choice(characters) for i in range(ranged))
        print("your password is: " + password)

    # creating an if statement so as to switch between the different strength selected
    if selected_option == 1:
        get_password(6)
    elif selected_option == 2:
        get_password(9)
    elif selected_option == 3:
        get_password(11)
    else:
        get_password(12)


# calling the main function so as to be executed
main()
