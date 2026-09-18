# Leap year checking in Python

year = int(input("Enter a year: "))

# A leap year is divisible by 4,
# but if divisible by 100, it must also be divisible by 400
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
