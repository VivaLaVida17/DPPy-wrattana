#!/usr/bin/env python3
import sys

sysLen = len(sys.argv)

if sysLen <= 2 :
  print("none")
else:
  for i in range(sysLen ,1 ,-1):
    print(sys.argv[i-1])