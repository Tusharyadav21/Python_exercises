# To check input character is an alphabet or not.

def check_alphabet(c):
    if (c>='a' and c<='z') or (c>='A' and c<='Z'):
        print("Yes, It's an alphabet.")
    else:
        print("No, It's not an alphabet.")


c = input("Enter a Character : ")
check_alphabet(c)
