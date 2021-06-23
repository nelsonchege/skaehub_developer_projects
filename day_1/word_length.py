# create a function that takes an argument of a word
def word_length(word_e):
    # Split a string into a list using .split()
    word = word_e.split()
    # when running this function it will return the length of the word
    return len(word[-1])
length=word_length(input("enter a word"))
# print the result of the fuction
print(f"your word has a length of:{length}")