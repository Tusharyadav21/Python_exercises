# Calculate percentage and grade according to following:
a1 = float(input("Enter the Physics marks : "))
a2 =float(input("Enter the Chemistry marks : "))
a3= float(input("Enter the Biology marks : "))
a4=float(input("Enter the Mathematics marks : "))
a5= float(input("Enter the Computer marks : "))
s= a1+a2+a3+a4+a5
p =(s*500)/100
if(p>=90):
    print("Grade A")
elif(p>=80):
    print("Grade B")
elif(p>=70):
    print("Grade C")
elif(p>=60):
    print("Grade D")
elif(p>=50):
    print("Grade E")
else:
    print("Grade F")