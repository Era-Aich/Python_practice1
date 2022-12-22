# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:57:29 2022

@author: computer market
"""

ample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for k in keys:
    ample_dict.pop(k)
print(ample_dict)