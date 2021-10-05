# Check Armstrong Number
n = input("Enter a number : ")
order = len(n)
num = int(n)
sum = 0

temp = num
while temp>0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(num," is a Armstrong Number.")
else:
    print(num, " is NOT an Armstrong Number.")
