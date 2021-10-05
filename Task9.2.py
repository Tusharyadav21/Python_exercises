# Number Divisibility by 5 and 11.

number = int(input("Enter a number : "))

if (number % 5 == 0) and (number % 11 == 0):
    print("Divisible by both.")
elif number % 11 == 0:
    print("Only divisible by 11.")
elif number % 5 == 0:
    print("Only divisible by 5.")
else:
    print("not divisible")