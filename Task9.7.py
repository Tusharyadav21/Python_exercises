# To check whether a character is uppercase or lowercase alphabet.

n = input("Enter an alphabet : ")[0]
if n.islower():
    print(n, " is a lowercase alphabet.")
elif n.isupper():
    print(n, " is a uppercase alphabet.")
else:
    print(n, " is an invalid character.")