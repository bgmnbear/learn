# Object metaphor
from datetime import date

today = date(2011, 9, 12)

print(str(date(2011, 12, 2) - today))

print(today.year)

print(today.strftime('%A, %B %d'))


# Raw data type
print(type(today))