from src.SimpleStackArray import *
# from src.SimpleStack import *


s = StackArray(10)

print(len(s)) # 0

print(s.isEmpty()) # True

print(s) # [ ]

s.push(10)
s.push(20)

print(s) # [ 10, 20]

print(s.pop()) # 20

s.push(30)

print(s) # [ 10, 30 ]

print(s.peek()) # 30

print(s) # [ 10, 30 ]

print(s.isEmpty()) # False

print(s.isFull()) # False

s.push(40)
s.push(41)
s.push(42)
s.push(43)
s.push(44)
s.push(46)
s.push(47)
s.push(48)

print(s.isFull()) # True