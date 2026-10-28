#!/usr/bin/env python3
import sys

sysLen = len(sys.argv)
val = ""

if sysLen == 1 :
  print("none")
else:
  count = sys.argv[1].count("z")
  for i in range(count):
    val = val+"z"
  print(val)