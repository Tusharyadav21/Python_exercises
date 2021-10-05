# To Print all multiples of 3 and 5 in an Interval
x = int(input("Enter the interval : "))
for x in range(0, x + 1):
    if x % 3 == 0 and x % 5 == 0:
        print(x)