#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:40:17 2019

@author: davidpokrajac
"""


#Exceptions example

A=[1,2,3,4]

ind=input('index')

try:
    index=int(ind) #Which kind of problem may arise here? ind
    #may not be a string convertible to integer
except ValueError:
    print('Sorry, you should have entered an integer number. Wrong index:',ind)
    
try:
    print(A[index])
except IndexError:
    print('Sorry, index', index, 'outside the range',-len(A),':',len(A)-1)
    

#Alternatively, combined (but less puristic)
    
    
    
A=[1,2,3,4]

ind=input('index')

try:
    print(A[int(ind)]) #Which kind of problem may arise here? ind
    #may not be a string convertible to integer
except IndexError:
    print('Sorry, index', ind, 'outside the range',-len(A),':',len(A)-1)

except ValueError:
    print('Sorry, you should have entered an integer number. Wrong index:',ind)



#
# Second example: key error, when searching dict for a non-existing key
#
SearchDictionary={'Peter':1,'Joe':2}
Key=input()
try:
    print(SearchDictionary[Key])
except KeyError:    
    print('There is no key ',Key)
    
#
# Numerical errors
#

try:
    0/0
except  ZeroDivisionError:
    print('Not defined')
    
a=100.
i=1000
try:
    a**i
except  OverflowError:
    print('Too large number')
    
#File handling error
    
FileName=input('Enter file name')

try:
    with open(FileName) as f:
        pass
except FileNotFoundError:
    print('The file does not exist')
    
#Advanced and bonus!
#Creation of customized exception.
#We need inherit from BaseException class (inheritance from Exception also seems to work)
class MyException(BaseException):
    pass

def Fun(x):
    if x>10:
        raise MyException('X is larger than 10')
    pass
