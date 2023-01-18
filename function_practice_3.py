# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 11:53:37 2023

@author: asus
"""

#Write a Python function to multiply all the numbers in a list.

def mul(*nums):
    total=1
    for i in nums:
        total=total*i
        print(total)
    
mul(2,3,4,5,6,7,8)