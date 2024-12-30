#show the month dates from calender
import calendar

try:
    y = int(input("INPUT THE YEAR: "))
    m = int(input("INPUT THE MONTH: "))
    
    # Check if the month is valid
    if m < 1 or m > 12:
        print("Invalid month! Please enter a value between 1 and 12.")
    else:
        print(calendar.month(y, m))

except ValueError:
    print("Invalid input! Please enter valid integers for the year and month.")
