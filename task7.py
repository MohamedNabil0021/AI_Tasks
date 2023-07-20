# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 23:33:07 2023

@author: Mohamed
"""

# Task7

def even_numbers(*numbers):
    
    even = []
    
    for number in numbers:
        
        if number % 2 == 0:
            
            even.append(number)
    
    
    print(even)


even_numbers(2,4,5,6,7,8)
