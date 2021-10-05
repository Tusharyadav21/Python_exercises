# To input week number and print weekday.
def check(week):
    weekdays = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    if week < 8:
        print(weekdays[num])
    else:
        print("invalid input")



num = int(input("Enter the week day (1-7) : "))
check(num)
