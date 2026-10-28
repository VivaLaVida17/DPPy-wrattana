#!/usr/bin/env python3
import sys

def downcase_it(val):
  return val.lower()

sysLen = len(sys.argv)

if sysLen == 1 :
  print("none")
else:
  for i in range(1 , sysLen):
    print(downcase_it(sys.argv[i]))