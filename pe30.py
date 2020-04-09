#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 21:04:19 2018

@author: sam
"""

n = 2
big = 0
while n > 1 and n < 1000000:
    digits = [int(d) for d in str(n)]
    print('Retrieving result')
    #print(digits)

    ans = 0
    for d in digits:
        add = pow(d,5)
        #print(d,"=",add)
        ans += add
    if n == ans:
        print(ans)
        big += ans
    n += 1      
print("Answer= ", big)
