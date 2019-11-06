#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:38:33 2019

@author: davidpokrajac
"""

g = (x**2 for x in range(4))
print(type(g)) #s we can see g is a generator

next(g) #will return the FIRST value in the generator
#We can iterate through g, note that we list the remaining 3 values, the first one is already used
for _ in g:
    print(_)
    
#If we try iterating again, we do not get anything, we exhausted g
for _ in g:
    print(_)

try:
    next(g)
except StopIteration:
    print('Dude, you exhausted the generator')    