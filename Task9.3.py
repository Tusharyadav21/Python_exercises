# To check Input Year is a Leap Year or not.
def checkYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Driver Code
year = int(input("Enter a Year : "))
if (checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")