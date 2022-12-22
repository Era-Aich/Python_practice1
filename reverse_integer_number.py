# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:50:52 2022

@author: computer market
"""


n=int(input("Enter the integer number"))

rev_num=0

while(n>0):
    rem = n%10
    rev_num = (rev_num*10) +rem
    n=n//10
    print(rev_num)
