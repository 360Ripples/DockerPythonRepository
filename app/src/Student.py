# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 22:57:24 2021

@author: shanmu
"""
class Student:
    def __init__(self,id,name,address):
        self.id=id
        self.name=name
        self.address=address
        
    def __str__(self):
        return str(self.id) + "--" + self.name+ "--" + self.address
