#!/usr/bin/env python3
import sys

sysLen = len(sys.argv)

if sysLen == 1 :
  print("none")
else:
  print(f"parameters: {sysLen -1}")
  for i in range (1 , sysLen ):
    print(f"{sys.argv[i]}: {len(sys.argv[i])}")