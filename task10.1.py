# To Check Palindrome Number
new = input("Enter the number/string : ")

if new == new[::-1]:
    print(new, " The number/string is a Palindrome.")
else:
    print(new, " The number/string is NOT a Palindrome.")