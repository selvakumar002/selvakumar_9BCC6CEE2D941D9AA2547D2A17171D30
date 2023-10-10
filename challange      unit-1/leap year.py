Year = int(input(“Enter a year: “))
If (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    Print(year, “is a leap year”)
Else:
    Print(year, “is not a leap year”)

# Input: Enter a year: 2012
# Output: 2012 is a leap year