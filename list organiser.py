# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 11:07:38 2020

@author: Robin
"""
import math
def load_a_list_of_ints():
    """
    Loads a list of integers by first asking for its length.
    """
    L = list()
    n = int(input("The number of list elements: "))
    for k in range(n):
        L.append(int(input(str(k+1) + ". element: ")))
    return L
def reverse_list():
    x.append(1)
    for i in range(math.ceil(len(x)/2)):
        x[len(x)-1] = x[i]
        x[i] = x[len(x)-2-i]
        x[len(x)-2-i] = x[len(x)-1]
    x[len(x)-1] = "e"
    x.remove("e")
    print(x)
def sort_list():
    s = x
    p = []
    for i in range(len(x)):
        p.append(min(s))
        s.remove(min(s))
    return p
def find_in_list():
    p = sort_list()
    el = input("Find in list")
    try:
        print(p.index(int(el)))
    except:
        print("None")
x = load_a_list_of_ints()
find_in_list()
