# To input all sides of a triangle and check whether triangle is valid or not.
a = float(input("Enter the length of side of a triangle : "))
b = float(input("Enter the length of side of a triangle : "))
c = float(input("Enter the length of side of a triangle : "))

if (a+b>c and a+c>b and b+c>a):
    print("Valid triangle")
else:
    print("Invalid triangle")