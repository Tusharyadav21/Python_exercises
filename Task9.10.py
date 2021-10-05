# To input angles of a triangle and check whether triangle is valid or not.
x = float(input("Enter the angle of first side of a triangle : "))
y = float(input("Enter the angle of second side of a triangle : "))
z = float(input("Enter the angle of third side of a triangle : "))

if ((x+y+z)%180) == 0:
    print("Valid triangle")
else:
    print("Invalid triangle")