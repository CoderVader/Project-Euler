#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 17:41:39 2018

@author: sam
"""

def fact_sum(n):
    if n == 0:
        return 1
    else:
        return n * fact_sum(n-1)
    
def getSum(x):
    sum = 0
    while (x != 0): 
        sum += int(x % 10)
        x = int(x/10)
    return sum
 
num = 100
#Finding the Factorial
fact = fact_sum(num)
print(fact)  
#Summing the Factorial
num = fact
add = getSum(num)
print(add)  

