#!/usr/bin/env python3

def add_one(val):
  result = val + 1
  return result

valInit = 17
print(f"valInit = {valInit}")
print("call add_one method")
valInit = add_one(valInit)
print(f"valInit After call add_one = {valInit}")
