# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 23:29:29 2023

@author: Mohamed
"""

# Task4

def length (*strings):
    
    max_length=0
    for lists in strings:
        if len(lists)>max_length:
            max_length=len(lists)
            new_max=lists
    
    print(f"the maximum length is {new_max} and the length of this is {len(new_max)}")



length("muhammed","mostafa","ali","mina")