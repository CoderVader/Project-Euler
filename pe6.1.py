#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 00:41:49 2018

@author: sam
"""
# better solution

sq_sum = 0
sum_sq = 0
for i in range(1,101):
    sum_sq += i ** 2
    sq_sum += i
    diff = (sq_sum ** 2) - sum_sq
#print(sum_sq)
#print(sq_sum)
print(diff)    
    