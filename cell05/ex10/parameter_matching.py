#!/usr/bin/env python3
import sys

sysLen = len(sys.argv)

if sysLen == 1 :
  print("none")
else:
  val = input("What was the parameter? ");
  if val == sys.argv[1] :
    print("Good job!")
  else:
    print("Nope, sorry...")