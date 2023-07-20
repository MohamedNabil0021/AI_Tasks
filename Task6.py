# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 23:32:33 2023

@author: Mohamed
"""


# Task6

def palindrome(*strings):
    for string in strings:
        
        if string[::1]==string[::-1]:
            print("true")
        else :
            print("false")
palindrome("mohamed")
