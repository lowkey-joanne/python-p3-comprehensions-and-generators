#!/usr/bin/env python3

def return_evens(data):
  return [num for num in data if num % 2 == 0]

def make_exclamation(data):
  return [sentence + '!' for sentence in data]
