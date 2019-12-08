#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
#Class Vector with property vec which is a list of vector elements
#Properties norm2: to calculate Euclidean norm (squared root of sum of squared elements); to change the norm by
#normalizing the vector
#norm1 to calculate the sum of absolte values but not to modify it
#
#Implement addition of two vectors, addition of a vector to a scalar, and addition of a scalar to a vector
#using add and radd 
#
#Implement alternate constructor, that generates a vector by repeat a scalar (Specify the scalar and number of repetitions)
#Use classmethod

#Using @total_ordering, implement comparison of vectors by their norm2
#we need implement methods __lt__ and __eq__

#Using __str__ method, write informal representation of the class, e.g., for a vector [3,4],
#str(v) will print 'Vector: [3, 4] with norm 5.0'
#
#Using __repr__ write formal representation of the class. For a=Vector([1,2,3,4]), shall return string 'Vector([1,2,3,4])'
#such that eval(repr(v)) generates the vector v
#
#Class Matrix as a subclass of Vector
#
#Specify a constructor that initializes data attribute of a matrix. The constructor takes 3 attributes:
#list of elements and dimensions M and N of the matrix. The data is a list of M lists, each of N elements
#e.g., Matrix([1,2,3,4,5,6],3,2) will have data attribute [[1, 2], [3, 4], [5, 6]]

#
#Class matrix has attributes M and N (number of elements horizontally and vertically)
#Use properties to write getter for these attributes

#Define a norm of the matrix as the square root of sum of its squared elements


#Define alterate constructor from_vectors that will construct a matrix from list of vectors
#(each element of the list will be one row of a matrix)

#Other method override with pass

import math
from functools import total_ordering #We must import that
from math import pi

@total_ordering #To enable ordering
class Circle(object):

    def __init__(self, radius):
        self.radius = float(radius)


    def __repr__(self):
        return ('Circle with radius: {0:.2f} and area of: {1:.2f}'
                .format(self.radius, self.area))

    def __str__(self):
        return ('Circle with radius: {0:.2f} and area of: {1:.2f}'
                .format(self.radius, self.area))

    @classmethod
    def from_d(cls, diameter):
        return cls(diameter / 2)

    @property
    def diameter(self):
        return 2*self.radius

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property
    def area(self):
        return self.radius**2*pi

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other

    def __lt__(self, other):
        return self.radius < other

    def __gt__(self, other):
        return self.radius > other
    
mycirle1 = Circle(4)
mycirle2 = Circle(6)
mycirle3 = Circle(8)
    

    