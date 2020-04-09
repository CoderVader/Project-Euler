#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 19:35:57 2018

Solution for problem 2. This problem gives the
sum of even valued fibonacci numbers from 1 to 4 million.

difficulty : easy

@author: sam
"""

# First Method
a,b =1,1
total = 0
while a <= 4000000:
    if a % 2 == 0:
        total += a
    a, b = b, a + b
print(total)    

# Second Method

cache = {}
def fib(n):
    cache[n] = cache.get(n, 0) or (n <= 1 and 1 or fib(n-1) + fib(n-2))
    return cache[n]

n = 0
x = 0
while fib(x) <= 4000000:
    if not fib(x) %2 : n = n + fib(x)
    x = x + 1
print(n)   