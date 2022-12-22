# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:39:14 2022

@author: computer market
"""


sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']["student"]['marks']['history'])