#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 20:17:35 2018

This program is the sum of the digits of the value 
attained when 2 is raised 1000 times.

@author: sam
"""

n = 2 ** 1000
digits = [int(d) for d in str(n)]
#print(digits)

add = digits
ans = sum(add)
print(ans) 


