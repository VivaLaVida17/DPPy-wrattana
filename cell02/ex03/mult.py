#!/usr/bin/env python3

fNumber = int(input("Enter the first number:\n"))
sNumber = int(input("Enter the second number:\n"))
result = fNumber * sNumber
print( fNumber , "x" , sNumber , "=", result)

if result < 0:
  print("This result is negetive")
elif result > 0:
  print("This result is positive")
else:
  print("This result is both positive and negative")#!/usr/bin/env python3