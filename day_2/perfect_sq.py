# importing the math library
import math

# user enters the number
number = int(input("Enter the Number:"))
# this method of math.sqrt()is from import that gives the square_root
square_root = math.sqrt(number)
# i add 0.5 becouse when you enter  a large number the sqrt() can give a float instead of an int
# for a perfect square it should be a product of whole numbers
# if the square of the number that was rooted before then the number is not a perfect square
if int(square_root + 0.5) ** 2 == number:
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")