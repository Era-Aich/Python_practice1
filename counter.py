# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 09:38:51 2022

@author: computer market


"""

from collections import Counter

c= Counter(['a','b','a','c','b',1,1,2,3,5,5])

c.update("ddm")

c.subtract('aabb')

print(c)