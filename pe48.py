#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 01:27:24 2018

@author: sam
"""

add = 0    
for num in range(1,1000):
    a = pow(num,num)
    print(num,"=", a)
    add += a
print(add)
digits = [int(d) for d in str(add)]
print(digits[-10:])    
    