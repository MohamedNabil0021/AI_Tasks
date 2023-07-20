# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 23:30:02 2023

@author: Mohamed
"""

# Task5

def average (*numbers):
    
    z=0
    for n in numbers:
        z+=n/len(numbers)
    
    print(z)    


average(4,8,6,7,5,8)