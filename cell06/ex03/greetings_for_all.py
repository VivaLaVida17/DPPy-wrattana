#!/usr/bin/env python3

def greetings(name=""):
  if isinstance(name, str):
    if(name == ""):
      print("Hello, noble stranger.")
    else:
      print(f"Hello, {name}")
  elif isinstance(name , int):
    print("Error! It was not a name.")


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)