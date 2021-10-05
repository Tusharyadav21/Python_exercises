# To check a number is positive negative or zero
def check_num(number):
    if number < 0:
        print("Negative : ", number)
    elif number > 0:
        print("Positive : ", number)
    else:
        print("Zero")


number = float(input("Enter a number : "))
check_num(number)

