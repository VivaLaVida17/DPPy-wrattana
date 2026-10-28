#!/usr/bin/env python3

import sys

def shrink(val):
  
  return enlarge(val[0:8])

def enlarge(val):
  if len(val) < 8 :
    return val + ("Z" * (8 - len(val)))
  else:
    return val

sysLen = len(sys.argv)

if sysLen == 1 :
  print("none")
else:
  for i in range(1 , sysLen):
    print(shrink(sys.argv[i]))