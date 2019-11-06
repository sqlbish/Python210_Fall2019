#!/usr/bin/env python3
"""
Created on Mon Nov  4 16:08:24 2019

@author: Bishal.Gupta
"""

import string


def load_file():
    with open('Sherlock1.txt','r') as f:
        read_data = f.read()
    f.closed
    True
    # Replace new-line
    read_data = read_data.replace("\n",'')
    # strip out punctuation
    punctuation = string.punctuation

    for letter in read_data:
        if letter in punctuation:
            read_data = read_data.replace(letter, ' ')

    # split words into a list
    wordslist = read_data.split()

    return wordslist


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    for i in range(len(words)-2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        pair = tuple(pair)
        
        # build up the dict here!
        trigrams.update({pair : follower})
        trigrams.setdefault(pair, []).append(follower)


    return trigrams ##this is out of scope

        
if __name__ ==  "__main__":
    wordlist1 = load_file()
    trigrams1 = build_trigrams(wordlist1)
    print(trigrams1)
    
