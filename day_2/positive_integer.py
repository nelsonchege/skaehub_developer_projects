def checkPowerOf4(number):
    # (n & (n - 1)) == 0) this function checks if n is a power of two
    # If the number is a power of two, then only 1 bit will be set in its binary representation.
    # If we subtract 1 from a number which is power of 2, then all the bits after the set-bit
    # (there is only one set bit as per point-1) will become set and the set bit will be unset. i.e:
    # a power of 4 has a remainder of 1 when it is divided by 3
    return ((number & (number - 1)) == 0) and (number % 3 == 1)


number = int(input("enter number here:"))

if checkPowerOf4(number):
    print(number, "is a power of 4")
else:
    print(number, "is not a power of 4")
