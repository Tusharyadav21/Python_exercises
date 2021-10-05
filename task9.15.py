# To input electricity unit charges and calculate total electricity bill according to the given condition:
unit = int(input("Enter the no. of units consumed : "))
a = 0
if unit > 0:
    if unit >= 50:
        a = 0.5 * 50
    else:
        a = 0.5 * unit
    unit = unit - 50
if unit > 0:
    if unit > 100:
        a = a + (0.75 * 100)
    else:
        a = a + (0.75 * unit)
    unit = unit - 100
if unit > 0:
    if unit > 100:
        a = a + (1.2 * 100)
    else:
        a = a + (1.2 * unit)
    unit = unit - 100
if unit > 0:
    a = a + (1.5 * unit)

a = a + (a * 0.2)
print("The total cost is : ",a)
