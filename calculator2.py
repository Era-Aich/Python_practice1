# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 07:06:03 2023

@author: asus
"""

class Calculator():
    
    "Addition,Subtraction,Multiplication,Division"
    
    '''def _init_(self,a,b):
          self.a=a
          self.b=b
          
    '''
       
    
    def add(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b
    
    def mul(self,a,b):
        return a*b
    
class Mycal(Calculator):
    
    '''def _init_(self,a,b,c):
a=int(input("Enter A:"))
b=int(input("Enter B:"))
        self.a=a
        self.b=b
        self.c=c
        
        '''
        
    def add(self,a,b,c):
        return a+b+c
    
    def cube (self,a):
        return a*a*a
    
a=int(input("Enter A: "))
b=int(input("Enter B:"))
c=int(input("Enter C:"))  

result=Mycal()


temp=result.add(a,b,c)  
print(temp)
    