# To input any character and check whether it is alphabet, digit or special character.

def check_character(c):
    if c.isalpha():
        print(c, " is an alphabet.")
    elif c.isdigit():
        print(c, " is a number.")
    else:
        print(c, " is a special character" )


a = input("Enter a character : ")[0]
check_character(a)