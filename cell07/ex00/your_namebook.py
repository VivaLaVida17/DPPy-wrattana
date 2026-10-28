#!/usr/bin/env python3

def array_of_names(persons):
  result = []
  for person in persons:
    result.append(person.capitalize()+" "+persons[person].capitalize())
  return result

persons = {
  "jean": "valjean",
  "grace": "hopper",
  "xavier": "niel",
  "fifi": "brindacier"
}

print(array_of_names(persons))