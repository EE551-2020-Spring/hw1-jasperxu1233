#!/usr/bin/python

"""
Python Core object Types
"""

import math

def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Assign a string "EE551" to a variable x
    x = "EE551"
    print(x)
    
    # Assign a string "Stevens" to a variable y
    y = "Stevens"
    print(y)
    
    # Repeat variable y 5 times
    for a in range(0,5):
        print (y)
        
    # What is the length of z?
    length = len(z)
    print(length)
    
    # Concatenate variable y with string " is good"
    m = y + " is good"
    print(m)
    
    # Replace "good" with "awesome" in variable m and assign it to a new variable n
    n = m.replace("good","awesome")
    print(n)
    
    return x, y, z, length, m, n


def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Stevens is awesome"

    # Split variable n on a delimiter space into a list of substrings
    p = n.split(" ")
    print(p)
    
    # Get all the items past the first of the third substring
    r = p[2].replace("awesome","wesome")
    print(r)
    
    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]
    import numpy as np
    A = np.mtarix("1,4,5;6,10,11;12,17,38")
    print(A)
    #or
    import numpy as np
    a = [1,4,5,6,10,11,12,17,38]
    A = np.array(a).reshape(3,3)
    print(A)
    
    # Collect the items in the last column of matrix A using list comprehension
    c = [i for i in a[2::3]]
    print(c)
    
    # Collect only the even items of the diagonal of matrix A using list comprehension
    d = [i for i in a[4::2]]
    print(d)
    
    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.
    o = [ord(i) for i in "Stevens"]
    print(o)
    return p, r, c, d, o


def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"
    a = {"fruit":"apple","quantity":4,"color":"green"}
    
    
    # Get the item in dictionary f that the key "fruit" maps to
    f = {"fruit":"apple","quantity":4,"color":"green"}
    value = f["fruit"]
    print(value)
    
    # Increase the quantity of f by 1
    # IMPLEMENT IT HERE
    f["quantity"] = f["quantity"]+1
    
    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    p["name"] = {"first_name":"Grace", "last_name":"Hopper"}
    p["jobs"] = ["scientist", "engineer"]
    p["age"] = 85
    print(p)
    
    # Add "programmer" to the list of jobs Grace has
    # IMPLEMENT IT HERE
    p["jobs"].append("programmer")
    print(p)
    
    # Get the third job Grace has that you recently added
    print(p["jobs"][2])
    
    # Use the sort() function to get sorted keys of amazing_grace in alphabetically ascending order
    k = []
    b = "amazing_grace"
    for  i in b:
        k.append(i)       
    k.sort()
    print(k)
    
    return a, f, p, k

numbers_and_strings()
lists()
dictionaries()





