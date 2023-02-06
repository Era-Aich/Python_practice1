# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 15:42:14 2023

@author: asus
"""


class Calculator:
    "Addition, Subtraction,Multiplication,Division"
    
    def _init_(self,a,b):
        self.a=a
        self.b=b
    
    def add(self,a,b):
        return a+b
    
    
    def sub(self,a,b):
        return a-b
    
    def multi(self,a,b):
        return a*b
    
    
mycal=Calculator()

temp=mycal.add(5,7)
print(temp)
temp=mycal.sub(2,3)
print(temp)
temp=mycal.multi(10,100)
print(temp)