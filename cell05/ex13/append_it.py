#!/usr/bin/env python3
import sys

sysLen = len(sys.argv)
val = "ism"

if sysLen == 1 :
  print("none")
else:
  for i in range(1 ,sysLen):
    if sys.argv[i].endswith(val) == 0 :
       print(sys.argv[i]+val)