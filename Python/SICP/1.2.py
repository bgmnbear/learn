# Nested structure
print('---Nested structure---')
m = max(min(1, -2), min(pow(3, 5), -4))
print(m)

# Name binding
print('---Name binding---')
radius = 10
from math import pi
area, circumference = pi * radius * radius, 2 * pi * radius
print(area)
print(circumference)

print(max)
f = max
print(f)
print(f(3, 4))
f = 2
print(f)

# Non-pure function
print('---Non-pure function---')
print(print(1), print(2))
