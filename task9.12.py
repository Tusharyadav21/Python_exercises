# To check whether the triangle is equilateral, isosceles or scalene triangle.
def check(x,y,z):
    if x==y==z:
        print('Equilateral Triangle')
    elif x==y!=z or x==z!=y or y==z!=x:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")

x = float(input("Enter the angle of first side of a triangle : "))
y = float(input("Enter the angle of second side of a triangle : "))
z = float(input("Enter the angle of third side of a triangle : "))

check(x,y,z)