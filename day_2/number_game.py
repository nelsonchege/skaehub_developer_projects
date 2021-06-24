# import random
import random
# random.randint() method from import generate random number and the argument
random_number = random.randint(1, 10)
#print(random_number)
# create empty variable so as to be used in the while loop
guess_number = None
while guess_number != random_number:
    # user enters the guess
    guess_number= int(input("guess a number between 1 and 10: "))
    # if statement compairs the user input to the number randomly selected
    if guess_number == random_number:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")
