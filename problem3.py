#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 22:30:51 2018

Solution for problem 3. Largest prime factor.
difficulty: easy

@author: sam
"""

n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i += 1

print(n)  


num = 2520
for i in range(1,num+1):
    if num%i == 0:
        print(i)
              
        