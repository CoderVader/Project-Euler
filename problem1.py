#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 19:23:21 2018

This program gives the solution for the sum of all multiples of
3 and 5 from 1 to 1000.
difficulty - very easy

@author: sam
"""
total = 0
for num in range(1,1000):
    if num%3 == 0 or num%5 == 0:
        total += num
print("The sum of all the numbers between 1-1000: ",total)        