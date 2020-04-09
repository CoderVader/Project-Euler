#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 00:47:17 2018

@author: sam
"""     

def fibon(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b, a+b
    return a

num = fibon(10)
print(num)
#total = 0
#if num %2 ==0:
#    total += num
    

    
        