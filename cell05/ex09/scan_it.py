#!/usr/bin/env python3
import sys

sysLen = len(sys.argv)

if sysLen <= 2 :
  print("none")
else:
  pos = sys.argv[2].count(sys.argv[1])
  print(pos)