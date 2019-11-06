#!/usr/bin/env python3

"""
Created on Sat Nov  2 11:40:11 2019
#Dictionary and Set lab
@author: davidpokrajac
"""

#Dictionaries

PersonData={"name":"Chris", "city":"Seattle","cake":"Chocolate"}
print(PersonData)
del PersonData['cake'] #REmoving key-value pair without printing it
print(PersonData) 
PersonData["fruit"]="Mango" #Adding a new key-value pair
print(PersonData)
print(PersonData.keys()) #Printing keys. If we need them as a list, we need convert, e.g., list (PersonData.keys())
print(PersonData.values())
print("cake" in PersonData.keys())
print("Mango" in PersonData.values())

NewDict={} #We initialize a new dictionary
for _ in PersonData.keys():
    NewDict[_]=PersonData[_].lower().count('t')
    #Since we use the looping variable only in this loop, we can use _ instead of, e.g., i,j, "key", etc.
    #We first convert each value into lower case, by using method lower(), and then count the number of occurances of character 't'
    #We put this count into a new dictionary

print(NewDict)


#Sets

N=20
Divisible2=set() #This is the way to initialize the empty set. If we try Divisible2={}, it will initialize DICTIONARY, as visible by type(Divisible2)
Divisible3=set()
Divisible4=set()
for i in range(1,N+1):
    if not i%2: # % is a remainder operation. i%2 gives remainder when we divide i by 2. If the remainder is 0, then not remainder is True and we add a number 
    #to the set
        Divisible2.add(i)
    if not i%3:
        Divisible3.add(i)
    if not i%4:
        Divisible4.add(i)

print(Divisible2)
print(Divisible3)
print(Divisible4)

print (Divisible2.issubset(Divisible3)) #IS set of numbers divisible by 2 a subset of those divisible by 3
print (Divisible4.issubset(Divisible2)) #IS set of numbers divisible by 4 a subset of those divisible by 2

#A fancy way to do the same
#Creates a dictionary with keys equal to divisors, in this case, 2,3,4.
#For each divisor we keep the set of number divisible by the divisor        
#This solution is easier to expand to other divisors (no copying of the code)
N=20

ListOfDivisors=[2,3,4]
Divisible={}
for _ in ListOfDivisors:
    Divisible[_]=set()

for i in range(1,N+1):
    for divisor in ListOfDivisors:
        if not i%divisor:
            Divisible[divisor].add(i)

        
for _ in ListOfDivisors:
    print(Divisible[_])


print (Divisible[2].issubset(Divisible[3]))
print (Divisible[4].issubset(Divisible[2]))


String='Python'

SetLetters=set()
for _ in String:
    SetLetters.add(_)

SetLetters.add('i')


#For reasons to be clear soon, I am going to create a function doing the same


def CreateSetFromString(string):
    SetLetters=set()
    for _ in string:
        SetLetters.add(_)
    SetLetters.add('i')
    return SetLetters

#The same task using this function
LettersFromString=CreateSetFromString("Python")
print(LettersFromString)


#Now, using the previously defined function to create "on fly" a set of letters and then to convert to a frozenset


LettersFromString=CreateSetFromString("Python")
FrozenSet=frozenset(CreateSetFromString("marathon"))

#There is much quicker way:
#Note that set and frozenset have iterable as an argument, so that they can directly convert a string (an iterable!)


SetLetters=set("Python") #Converts elements of the iterable into a set
FrozenSet=frozenset("marathon") #Converts elements of the iterable into a frozen set
#Note: sets and frozen sets are not subscriptable. They are not ordered, hence:
#something like SetLetters[2], FrozenSet[1] will not work (you will get TypeError, try that)
#However, sets and frozensets are iterable, so the following would work:

for _ in FrozenSet:
    print(_)

for _ in SetLetters:
    print(_)

#We can use set operations on sets and subsets. The type (class) of the object from which we utilize a method determine the type
#of the result
    
print(FrozenSet.union(SetLetters)) #Union of a frozen set and a set is a frozen set
print(type(FrozenSet.union(SetLetters)))
print(SetLetters.union(FrozenSet)) #Union of a set and frozen set is a set
print(type(SetLetters.union(FrozenSet)))

print(FrozenSet.intersection(SetLetters)) #intersection of a frozen set and a set is a frozen set
print(type(FrozenSet.intersection(SetLetters)))
print(SetLetters.intersection(FrozenSet)) #intersection of a set and frozen set is a set
print(type(SetLetters.intersection(FrozenSet)))





        

