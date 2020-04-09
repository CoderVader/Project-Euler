#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 00:15:03 2018

@author: sam
"""

total1 = 0
total2 = 0
sum_sq = 0
sq_sum = 0
diff = 0
for i in range(1,101):
    total1 += i ** 2
    sum_sq = total1
    
    total2 += i
    sq_sum = total2 ** 2
    
    diff = sq_sum - sum_sq
    
    
print(diff)
    