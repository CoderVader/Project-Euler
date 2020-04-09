#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 23:54:57 2018

@author: sam
"""

n = 2

while n > 1 and n < 10000:
    for i in range(1,10):         
        if n % i == 0:
            print(i, "=" , n)
    n +=1        