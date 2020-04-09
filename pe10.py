#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 23:54:57 2018

Description: Program to find the sum of primes that
1 to 2 million
@author: sam
"""

# number to find summation of all primes below number
lim = 2000000

# create a set excluding even numbers
numbers = set(range(3, lim + 1, 2)) 

for number in range(3, int(lim ** 0.5) + 1):
    if number not in numbers:
        #number must have been removed because it has a prime factor
        continue

    num = number
    while num < lim:
        num += number
        if num in numbers:
            # Remove multiples of prime found
            numbers.remove(num)

print(2 + sum(numbers))