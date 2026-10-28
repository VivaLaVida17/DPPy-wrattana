#!/usr/bin/env python3

def find_the_redheads(family):
  result = []
  for person in family:
    if(family[person] == "red"):
      result.append(person)
  return result
  

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))