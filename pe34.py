#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 20:38:58 2018

@author: sam
"""

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)

n = 146
digits = [int(d) for d in str(n)]
print(digits)

add = 0
big_add = 0
for d in digits:
    f = fact(d)
    add += f
    print(f)
print('Sum:' ,add)
if add == n:
        print("true")
    
else:
    print('false')
        
    
        