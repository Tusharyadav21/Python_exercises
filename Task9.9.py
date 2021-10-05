# To count number of notes for each note in given amount.
amount = int(input("Enter the amount you want to withdraw : "))
temp = amount


note_2000 = amount // 2000
temp = amount % 2000
note_500 = temp // 500
temp = temp % 500
note_200 = temp // 200
temp = temp % 200
note_100 = temp // 100
temp = temp % 100
note_50 = temp // 50
temp = temp % 50
note_20 = temp // 20
temp = temp % 20
note_10 = temp // 10
temp = temp % 10
note_5 = temp // 5
temp = temp % 5


print("Number of 2000 rupees notes:",note_2000)
print("Number of 500 rupees notes:",note_500)
print("Number of 200 rupees notes:",note_200)
print("Number of 100 rupees notes:",note_100)
print("Number of 50 rupees notes:",note_50)
print("Number of 20 rupees notes:",note_20)
print("Number of 10 rupees notes:",note_10)
print("Number of 5 rupee coins:",note_5)
print("Number of change remaining:",temp)