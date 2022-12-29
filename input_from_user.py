# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 19:57:50 2022

@author: computer market
"""

from array import *



arr=array('i',[])
n=int(input("Enter the length of the array"))

for i  in range(n):
    x=int(input("Enter the element"))
    arr.append(x)
    
print(arr)