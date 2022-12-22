# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:17:29 2022

@author: computer market
"""

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict["location"]=sample_dict.pop("city")
print(sample_dict)