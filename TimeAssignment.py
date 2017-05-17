"""
NAME: KASULE ASHIRAF
STUDENT NO: 214002689
REG NO: 14/U/18264/EVE
"""

import calendar
print("This Program is intended to produce the exact date you were born")
print("................................................................")

dy = int(input("Please type in your day: "))
mth = int(input("Please type in your month: "))
yr = int(input("Please type in your year: "))

#this outputs the day in form of numbers from 0 - 6

day_num = calendar.weekday(yr, mth, dy)
actual_date = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("You were born on ", actual_date[day_num])


input("press Enter to exit")

