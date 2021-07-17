# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 11:38:32 2021

@author: HP
"""


name = input("enter your name: ")
print(name)
a = int(input("enter the english marks: "))
b = int(input("enter the maths marks: "))
c = int(input("enter the physics marks: "))
d = int(input("enter the chemistry marks: "))
e = int(input("enter the social marks: "))
total = (a+b+c+d+e)
print(total)
percentage = (total/500*100)
print(percentage)
average = (total/5)
print(average)