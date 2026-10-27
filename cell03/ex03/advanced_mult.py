#!/usr/bin/env python3
import sys

value = len(sys.argv)

if value > 1 :
  print("none")
else:
  for i in range(11):
    print(f"Table de {i} : " , *(j * i  for j in range(11)))
