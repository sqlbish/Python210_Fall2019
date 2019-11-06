#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:57:34 2019

@author: davidpokrajac
"""

#
#Counter
#
from collections import Counter

#Counter has as an input hashable items, and as an output dictionary 
#where for each element returns its count
a=[12,3,22,12,4,5,24]
print(Counter(a))

print(Counter((2,2,3)))

cc=Counter(a)
type(cc)

#Methods:
#.most_common()
#.elements

cc[12] #Counter of a specific key

#
# Named tuples
#
from collections import namedtuple

Coordinates=namedtuple('Coordinates','x,y')
Point1=Coordinates(1,2)
Point2=Coordinates(y=10,x=20)

print(Point1[0])
print(Point1.x)
print(Point2)

#
#deque module
#Actually, supports queue and stack

from collections import deque
dir(deque) #tells us what is available

a=deque(['a',2,3,4,112]) #creates a queue from iterable (in this case, list)

 a.extend([44,555]) #extend appends the argument (an iterable) at the right side
 a.extendleft(['LeftSide']) #extends on the left side

a.pop() #pops the rightmost element
a.leftpop() #pops the leftmost element

a.insert(3,'Here it is') #Inserts at the specific place

a.index(33) # returns index of an element if it is in the data structurem otherwise ValueError


#
#OrderedDict
#Dictionary that remembers insertion order

from collections import OrderedDict 


#popitem returns key and value, pop returns just a key

print ('Regular dictionary:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['d'] = 'D'
d['e'] = 'E'
d['c'] = 'C'

for k, v in d.items():
    print (k, v)
