#!/usr/bin/env python3
import sys

sysLen = len(sys.argv)

if sysLen == 1 :
  print("none")
else:
  for i in range(1, sysLen):
    print(sys.argv[i].upper())